import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math



def cost_function(x, y, w, b):
    m = x.shape[0]

    cost = 0
    for i in range(m):
        f_wb = w * x[i] + b
        cost += (f_wb - y[i]) ** 2
    return cost / m


def gradient_function(x, y, w, b):
    """
    Computes the gradient for linear regression 
    Args:
        x (ndarray (m,)): Data, m examples 
        y (ndarray (m,)): target values
        w,b (scalar)    : model parameters  
    Returns
        dj_dw (scalar): The gradient of the cost w.r.t. the parameters w
        dj_db (scalar): The gradient of the cost w.r.t. the parameter b     
    """
    dj_dw = 0
    dj_db = 0

    m = x.shape[0]

    for i in range(m):
        f_wb = w * x[i] + b
        dj_dw += (f_wb - y[i]) * x[i]
        dj_db += (f_wb - y[i])

    dj_dw /= m
    dj_db /= m

    return dj_dw,  dj_db


def gradient_descent(x, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function):
    """
    Performs gradient descent to fit w,b. Updates w,b by taking 
    num_iters gradient steps with learning rate alpha
    
    Args:
      x (ndarray (m,))  : Data, m examples 
      y (ndarray (m,))  : target values
      w_in,b_in (scalar): initial values of model parameters  
      alpha (float):     Learning rate
      num_iters (int):   number of iterations to run gradient descent
      cost_function:     function to call to produce cost
      gradient_function: function to call to produce gradient
      
    Returns:
      w (scalar): Updated value of parameter after running gradient descent
      b (scalar): Updated value of parameter after running gradient descent
      J_history (List): History of cost values
      p_history (list): History of parameters [w,b] 
    """

    m = x.shape

    w = 0
    b = 0
    j_history = []
    p_history = []

    for i in range(num_iters):
        dj_dw, dj_db = gradient_function(x, y, w, b)
        w -= alpha * dj_dw
        b -= alpha * dj_db
        p_history.append([w, b])
        j_history.append(cost_function(x, y, w, b))

        if i % math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4}: Cost {float(j_history[-1]):8.2f}   ")
    return w, b, j_history, p_history


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

def model_plot(x_train, y_train):
    f_wb = w * x_train + b


    plt.scatter(x_train, y_train, marker='x', c='red', label='actual price')
    plt.plot(x_train, f_wb, color='blue', label='predicted price')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cars Price')
    plt.legend()
    plt.show()


def test_model(x_test, y_test, w, b):
    result = x_test * w + b
    m = x_test.shape[0]

    for i in range(m):

        millege = x_test[i] * sigma + mu
        print(f"actual price for {millege:8.2f} is : {y_test[i]:8} and the predicted price is {result[i]:8.2f}")


    plt.scatter(x_test, y_test, marker='x', c='red', label='actual price')
    plt.scatter(x_test, result, marker='.', c='blue', label='predicted price')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cars Price')
    plt.legend()
    plt.show()









df = pd.read_csv("data.csv")

train_df, test_df = split_df(df)


X_train = np.array(train_df['km'])
y_train = np.array(train_df['price'])

X_test = np.array(test_df['km'])
y_test = np.array(test_df['price'])




X_train, mu, sigma = zscore_normalize_features(X_train)
X_test, mu, sigma = zscore_normalize_features(X_test)

num_iters = 120000

w, b , J_history, p_history= gradient_descent(X_train, y_train, 0, 0, 0.0001, num_iters, cost_function, gradient_function)



test_model(X_test, y_test, w, b)

model_plot(X_train, y_train)





# # plt.plot(np.arange(0,num_iters,1), J_history, color='blue', label='cost per iteration')