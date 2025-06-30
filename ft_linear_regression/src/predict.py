from utils import get_model_params

def predict_car_price(w, b, mu, sigma):
    try:
        mileage = float(input("Enter the distance (in km) to predict the car price: "))
        if mileage < 0:
            raise Exception("distance must be a a positive number!")
        mileage_norm = (mileage - mu) / sigma
        return int(w * mileage_norm + b)
    except ValueError:
        raise Exception("distance must be a number!")


if __name__ == "__main__":
    try:
        model_params_filename = "./models/model_params.json"
        w, b, mu, sigma = get_model_params(model_params_filename)
        predicted_price = predict_car_price(w, b, mu, sigma)
        predicted_price = max(0, predicted_price)
        print(f"Predicted car price: {predicted_price}")
    except Exception as e:
        print(f"ERROR: {e}")
