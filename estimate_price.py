import argparse
import yaml


def estimate_price(mileage: int, theta_0: float, theta_1: float):
    print(type(mileage))
    print(type(theta_0))
    print(type(theta_1))
    estimated_price = float(theta_0) + (float(theta_1) * int(mileage))

    return estimated_price


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mileage')
    parser.add_argument('--param_yaml')
    args = parser.parse_args()
    with open(args.param_yaml) as param_data:
        params = yaml.safe_load(param_data)
        theta_0 = params["param"]["theta0"]
        theta_1 = params["param"]["theta1"]

    estimated_price = estimate_price(args.mileage, theta_0, theta_1)
    print("estimated_price: ", estimated_price)
