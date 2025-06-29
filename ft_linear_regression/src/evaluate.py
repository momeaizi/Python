import numpy as np
import pandas as pd
from utils import get_model_params





def model_precision(y_true, x, w, b, mu, sigma):
    x_norm = (x - mu) / sigma
    y_pred = x_norm * w + b
    return 1 - np.sum((y_pred - y_true) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2)


if __name__ == "__main__":
    try:
        df = pd.read_csv("./data/data.csv")


        X_train = np.array(df['km'])
        y_train = np.array(df['price'])


        model_params_filename = "./models/model_params.json"
        w, b, mu, sigma = get_model_params(model_params_filename)
        print("Model precision:")
        r2 = model_precision(y_train, X_train, w, b, mu, sigma)
        print(f"- R² Score: {r2}, {float(r2 * 100):8.2f}%")

    except Exception as e:
        print(f"ERROR: {e}")

