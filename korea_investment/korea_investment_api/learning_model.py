import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os as os
import pandas as pd
import tensorflow as tf
import yaml
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential
from korea_investment_api.quotes import Quotes
from korea_investment_api.token_management import TokenManagement
from sklearn.preprocessing import MinMaxScaler

with open("config.yaml", encoding="UTF-8") as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)

KOREA_INVESTMENT_BASE_URL = _cfg["KOREA_INVESTMENT_BASE_URL"]
KOREA_INVESTMENT_APP_KEY = _cfg["KOREA_INVESTMENT_APP_KEY"]
KOREA_INVESTMENT_APP_SECRET = _cfg["KOREA_INVESTMENT_APP_SECRET"]
CANO = _cfg["CANO"]
ACNT_PRDT_CD = _cfg["ACNT_PRDT_CD"]
ACCESS_TOKEN = ""


class LearningModel:
    def learning_model(self):
        # 데이터 로드
        # df = pd.read_csv(
        #     "/Users/kyu/Coding/VSCode/korea-investment-python/korea_investment/dataset/eth.csv"
        # )
        # # 필요한 feature만 선택
        # df = df[["Close"]]
        # print(df)

        ACCESS_TOKEN = TokenManagement.issue_korea_investment_token()

        daily_response = Quotes.get_domestic_stock_daily_prices(
            self, ACCESS_TOKEN, "005930"
        )

        data = []
        for values in daily_response["output"]:
            data.append([float(values["stck_clpr"])])

        pd_data = pd.DataFrame(data, columns=["stck_clpr"])
        # print(pd_data)

        # 데이터 전처리
        scaler = MinMaxScaler()
        df_scaled = scaler.fit_transform(pd_data)
        # print(df_scaled)

        # train/test 분리
        train = df_scaled[: int(len(df_scaled) * 0.8), :]
        test = df_scaled[int(len(df_scaled) * 0.8) :, :]
        # print(test)

        # LSTM 입력 형태로 변환
        def create_dataset(X, y, time_steps=1):
            Xs, ys = [], []
            for i in range(len(X) - time_steps):
                Xs.append(X[i : (i + time_steps), :])
                ys.append(y[i + time_steps])
            return np.array(Xs), np.array(ys)

        time_steps = 2
        X_train, y_train = create_dataset(train, train[:, 0], time_steps)
        X_test, y_test = create_dataset(test, test[:, 0], time_steps)
        # print(X_test)

        # LSTM 모델 정의
        model = Sequential()
        model.add(
            LSTM(
                128,
                input_shape=(X_train.shape[1], X_train.shape[2]),
                activation="relu",
                return_sequences=True,
            )
        )
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.LSTM(64, activation="relu"))
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.Dense(1))

        # 모델 컴파일
        model.compile(optimizer="adam", loss="mse")

        # 모델 학습
        history = model.fit(
            X_train,
            y_train,
            epochs=50,
            batch_size=16,
            validation_split=0.1,
            shuffle=False,
        )

        # 모델 예측
        y_pred = model.predict(X_test)

        # 결과 시각화
        plt.plot(y_test, label="True")
        plt.plot(y_pred, label="Predicted")
        plt.legend()
        # plt.show()

        directory_path = (
            "/Users/kyu/Coding/VSCode/korea-investment-python/korea_investment/images"
        )
        image_path = "/Users/kyu/Coding/VSCode/korea-investment-python/korea_investment/images/result.png"

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        if os.path.exists(image_path):
            i = 1
            while os.path.exists(f"{directory_path}/result_{i}.png"):
                i += 1
            os.rename(image_path, f"{directory_path}/result_{i}.png")

        plt.savefig(image_path)

        return {"code": 0, "message": "성공"}
