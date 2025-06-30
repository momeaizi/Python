import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from regression import LinearRegression
import json


def split_df(df):
    shuffled_df = df.sample(frac=1, random_state=42)  # Randomly shuffling the rows using a fixed random state (42)

    # Define the proportion for training and testing
    train_ratio = 0.8  # 80% for training
    test_ratio = 0.2   # 20% for testing

    # Calculate the number of rows for training and testing
    num_rows = shuffled_df.shape[0]
    train_rows = int(num_rows * train_ratio)
    test_rows = num_rows - train_rows

    # Split the shuffled DataFrame into training and testing sets
    train_df = shuffled_df[:train_rows]
    test_df = shuffled_df[train_rows:]

    # Optional: Reset the index of the new DataFrames
    train_df.reset_index(drop=True, inplace=True)
    test_df.reset_index(drop=True, inplace=True)

    return train_df, test_df

def zscore_normalize_features(X):
    """
    computes  X, zcore normalized by column
    
    Args:
    X (ndarray (m,n))     : input data, m examples, n features
    
    Returns:
    X_norm (ndarray (m,n)): input normalized by column
    mu (ndarray (n,))     : mean of each feature
    sigma (ndarray (n,))  : standard deviation of each feature
    """
    # find the mean of each column/feature
    mu     = np.mean(X, axis=0)                 # mu will have shape (n,)
    # find the standard deviation of each column/feature
    sigma  = np.std(X, axis=0)                  # sigma will have shape (n,)
    # element-wise, subtract mu for that column from each example, divide by std for that column
    X_norm = (X - mu) / sigma      

    return (X_norm, mu, sigma)


def model_plot(ax, X, x_norm, y_train, w, b):
    f_wb = w * x_norm + b
    ax.scatter(X, y_train, marker='x', c='red', label='actual price')
    ax.plot(X, f_wb, color='blue', label='predicted price')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Training Data')
    ax.legend()


def plot_cost(ax, J_history):
    ax.plot(np.arange(len(J_history)), J_history, color='blue')
    ax.set_title('Cost per Iteration')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Cost')



def plot_3d_cost_surface(ax, x_norm, y_train,):
    m = len(x_norm)

    # Define w and b range
    w_vals = np.linspace(-1300, -900, 100)
    b_center = np.mean(y_train)
    b_range = 2 * np.std(y_train)
    b_vals = np.linspace(b_center - b_range, b_center + b_range, 100)


    # Create grid
    W, B = np.meshgrid(w_vals, b_vals)
    Z = np.zeros_like(W)

    # Compute cost J(w, b)
    for i in range(W.shape[0]):
        for j in range(W.shape[1]):
            w = W[i, j]
            b = B[i, j]
            y_pred = w * x_norm + b
            Z[i, j] = np.sum((y_pred - y_train) ** 2) / (2 * m)

    # Plot surface
    ax.plot_surface(W, B, Z, cmap='viridis', alpha=0.8)
    ax.set_xlabel('w')
    ax.set_ylabel('b')
    ax.set_zlabel('Cost')
    ax.set_title('Cost Function Surface (J(w, b))')


def save_model_params(w, b, mu, sigma, file_name="./models/model_params.json"):
    model_params = {
        "w": w,
        "b": b,
        "mu": mu,
        "sigma": sigma
    }

    with open(file_name, 'w') as f:
        json.dump(model_params, f, indent=4)




if __name__ == "__main__":
    try:
        df = pd.read_csv("./data/data.csv")

        X = np.array(df['km'])
        y_train = np.array(df['price'])

        X_norm, mu, sigma = zscore_normalize_features(X)

        model = LinearRegression()
        w, b , J_history, p_history = model.fit(X_norm, y_train)

        save_model_params(w, b, mu, sigma)

        fig = plt.figure(figsize=(14, 10))
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 3, projection='3d')


        model_plot(ax1, X, X_norm, y_train, w, b)
        plot_cost(ax2, J_history)
        plot_3d_cost_surface(ax3, X_norm, y_train)

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Something went wrong: {e}")

