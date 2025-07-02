# 🚗 Car Price Prediction using Linear Regression

This project is a simple implementation of a **linear regression model** to estimate the **price of a used car based on its mileage (kilometers driven)**.

It was developed as an educational project to demonstrate how machine learning models can be built from scratch — without relying on libraries like `scikit-learn`.

---

## 📌 Project Description

The goal is to create two separate programs:

1. **Training Program**:
   - Reads a dataset of car mileages and prices.
   - Normalizes the input data using **Z-score normalization**.
   - Trains a **linear regression model** using **gradient descent**.
   - Saves the learned parameters (`w`, `b`, `mu`, `sigma`) in a `.json` file.
   - Generates graphs to visualize training results, including:
     - Predicted vs. actual prices
     - Cost per iteration
     - 3D cost surface

2. **Prediction Program**:
   - Loads the trained model parameters.
   - Takes user input (mileage).
   - Normalizes it using the same mean and std used during training.
   - Outputs the **predicted price** of the car.

---

This project also includes:
- Model evaluation using **R² Score (coefficient of determination)** and **RMSE (Root Mean Squared Error)**.
- Edge case handling (e.g., negative predictions).
- Modular code structure with separation of logic for training, prediction, evaluation, and utilities.

---

The goal is to help beginners understand the internal workings of linear regression and how real-world prediction models can be built and evaluated from the ground up.


---

## 🔧 Environment Setup

It's recommended to use a virtual environment for clean dependency management.

### 1. Create a virtual environment

```bash
python3 -m venv venv
````

### 2. Activate the environment


  ```bash
  source venv/bin/activate
  ```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Deactivate when done

```bash
deactivate
```

---

## 🚀 How to Use

### 1. 🧠 Train the Model

```bash
python src/train.py
```

This will:

* Normalize the dataset (`km` feature)
* Train a linear regression model
* Save the model parameters (`w`, `b`, `mu`, `sigma`) in `models/model_params.json`

---

### 2. 📊 Evaluate the Model

```bash
python src/evaluate.py
```

This prints:

* **R² Score** (model precision)
* **RMSE** (prediction error)

---

### 3. 🔮 Predict Car Price

```bash
python src/predict.py
```

This asks the user to input a mileage (in kilometers) and predicts the car price using the trained model.

---

## 📌 Example

```bash
$ python src/predict.py
Enter car mileage (in km): 25000
Predicted car price: 17500 $
```

---

## 🧠 Model Details

* Algorithm: **Linear Regression (manual implementation)**
* Normalization: **Z-score** on mileage
* Evaluation: **R² Score**, **RMSE**, 3D cost visualization
* Parameters saved: `w`, `b`, `mu`, `sigma`

---

## 📈 Visualizations

* Data scatter + fitted regression line
* Cost function surface (3D)
* Cost over iterations

---

## 📬 License

This project is for educational purposes and free to use.

---