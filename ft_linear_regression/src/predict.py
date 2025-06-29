from utils import get_model_params

def predict_car_price(w, b, mu, sigma):
    try:
        mileage = float(input("Enter the distance (in km) to predict the car price: "))
        mileage_norm = (mileage - mu) / sigma
        return int(w * mileage_norm + b)
    except ValueError:
        raise Exception("distance must be a number!")


if __name__ == "__main__":
    try:
        model_params_filename = "./models/model_params.json"
        w, b, mu, sigma = get_model_params(model_params_filename)
        predicted_price = predict_car_price(w, b, mu, sigma)
        print(f"Predicted car price: {predicted_price}")
    except Exception as e:
        print(f"ERROR: {e}")
