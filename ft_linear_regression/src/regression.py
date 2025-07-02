import math


class LinearRegression():
    def cost_function(self, x, y, w, b):
        m = x.shape[0]

        cost = 0
        for i in range(m):
            f_wb = w * x[i] + b
            cost += (f_wb - y[i]) ** 2
        return cost / (2 * m)


    def gradient_function(self, x, y, w, b):
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


    def gradient_descent(self, x, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function):
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

        print("Starting Linear Regression Training...")
        print(f"Initial w: {w_in}, b: {b_in}")
        print(f"Learning rate: {alpha}")
        print(f"Iterations: {num_iters}")
        m = x.shape

        w = w_in
        b = b_in
        j_history = []
        p_history = []

        for i in range(num_iters):
            dj_dw, dj_db = gradient_function(x, y, w, b)
            w -= alpha * dj_dw
            b -= alpha * dj_db
            p_history.append([w, b])
            j_history.append(cost_function(x, y, w, b))

            if i % math.ceil(num_iters / 10) == 0:
                print(f"Iteration\t{i:4}\t: cost =\t{float(j_history[-1]):8.2f}\t: w =\t{w:8.2f}\t: b =\t{b:8.2f}")
        
        print("Training complete.")
        print(f"Final parameters: w =\t{w:8.2f}\t: b =\t{b:8.2f}")
        print(f"Final cost: {float(j_history[-1]):8.2f}")
        return w, b, j_history, p_history


    def fit(self, X_train, y_train):
        return self.gradient_descent(X_train, y_train, 0, 0, 0.001, 6100, self.cost_function, self.gradient_function)
        
