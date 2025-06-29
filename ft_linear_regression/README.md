# 🚗 Car Price Prediction using Linear Regression

This project predicts the **price of a car based on its mileage** using a custom implementation of **linear regression** trained on a real dataset.

---

## 📁 Project Structure

```

car\_price\_prediction/
│
├── data/
│   └── data.csv                  # Dataset: car mileage and price
│
├── models/
│   └── model\_params.json         # Trained model parameters: w, b, mu, sigma
│
├── src/
│   ├── train.py                  # Trains the linear regression model
│   ├── evaluate.py               # Evaluates model precision (R², RMSE)
│   ├── predict.py                # Takes user input and predicts car price
│   ├── regression.py             # Custom linear regression implementation
│   └── utils.py                  # Utility functions (e.g., read model, normalize)
│
├── plots/                        # (Optional) Visualizations like cost surface
├── README.md                     # You are here
└── requirements.txt              # Dependencies

````

---

## 🚀 How to Use

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt
````

If `requirements.txt` is not created yet, install manually:

```bash
pip install numpy pandas matplotlib
```

---

### 2. 🧠 Train the Model

```bash
python src/train.py
```

This will:

* Normalize the dataset (`km` feature)
* Train a linear regression model
* Save the model parameters (`w`, `b`, `mu`, `sigma`) in `models/model_params.json`

---

### 3. 📊 Evaluate the Model

```bash
python src/evaluate.py
```

This prints:

* **R² Score** (model precision)
* **RMSE** (prediction error)
* Optional: visualizations of cost function and data fit

---

### 4. 🔮 Predict Car Price

```bash
python src/predict.py
```

This asks the user to input a mileage (in kilometers) and predicts the car price using the trained model.

---

## 🧠 Model Details

* Algorithm: **Linear Regression (manual implementation)**
* Normalization: **Z-score** on mileage
* Evaluation: **R² Score**, **RMSE**, 3D cost visualization
* Parameters saved: `w`, `b`, `mu`, `sigma`

---

## 📌 Example

```bash
$ python src/predict.py
Enter car mileage (in km): 25000
Estimated car price: 17500.34 $
```

---

## 📈 Sample Visualization

* Data scatter + fitted regression line
* Cost function surface (3D)
* Cost over iterations (if using gradient descent)

---

## 📬 License

This project is for educational purposes and free to use.

---
