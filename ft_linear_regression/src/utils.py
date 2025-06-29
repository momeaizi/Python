import json

def get_model_params(model_params_filename):
    with open(model_params_filename, 'r') as f:
        model_params_data = json.load(f)
    w = model_params_data.get('w', 0)
    b = model_params_data.get('b', 0)
    mu = model_params_data.get('mu', 0)
    sigma = model_params_data.get('sigma', 1)
    return w, b, mu, sigma


