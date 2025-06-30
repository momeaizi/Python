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
├── README.md                     # You are here
└── requirements.txt              # Dependencies

````

---

## 🔧 Environment Setup

It's recommended to use a virtual environment for clean dependency management.

### 1. Create a virtual environment

```bash
python3 -m venv venv
````

### 2. Activate the environment

* **Linux/macOS:**

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