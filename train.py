import argparse

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
from tqdm import tqdm


def read_data(csv_file_path: str):
    df = pd.read_csv(csv_file_path)
    mileage_list = df["km"].values.tolist()
    price_list = df["price"].values.tolist()

    return mileage_list, price_list


def calculate_cost_func(mileage_list, price_list, pred_theta_0, pred_theta_1):
    diff_sum = 0
    for i in range(len(mileage_list)):
        diff_sum += (
            price_list[i] - (pred_theta_1 * mileage_list[i] + pred_theta_0)
        ) ** 2

    return diff_sum / len(mileage_list)


def calculate_grad_0(mileage_list, price_list, pred_theta_0, pred_theta_1):
    diff_sum = 0
    for i in range(len(mileage_list)):
        diff_sum += price_list[i] - (pred_theta_1 * mileage_list[i] + pred_theta_0)

    return (-2) * diff_sum / len(mileage_list)


def calculate_grad_1(mileage_list, price_list, pred_theta_0, pred_theta_1):
    diff_sum = 0
    for i in range(len(mileage_list)):
        diff_sum += mileage_list[i] * (
            price_list[i] - (pred_theta_1 * mileage_list[i] + pred_theta_0)
        )

    return (-2) * diff_sum / len(mileage_list)


def normalize_range(data_list):
    norm_list = []
    min_data = min(data_list)
    max_data = max(data_list)
    for i in range(len(data_list)):
        norm_data = (data_list[i] - min_data) / (max_data - min_data)
        norm_list.append(norm_data)

    return norm_list


def reverse_before_normalization(target_value, data_list):
    min_data = min(data_list)
    max_data = max(data_list)
    ori_value = target_value * (max_data - min_data) + min_data

    return ori_value


def save_parameter(final_pred_theta_0, final_pred_theta_1, output_param_path):
    data = {
        "param": {"theta0": str(final_pred_theta_0), "theta1": str(final_pred_theta_1)}
    }

    with open(output_param_path, "w") as output_file:
        yaml.dump(data, output_file)


def train(csv_file_path: str, output_param_path: str):
    init_theta_0 = 0
    init_theta_1 = 0
    learning_rate = 0.01
    threshold = 0.00000001

    mileage_list, price_list = read_data(csv_file_path)
    norm_mileage_list = normalize_range(mileage_list)
    norm_price_list = normalize_range(price_list)
    pred_theta_0 = init_theta_0
    pred_theta_1 = init_theta_1
    iterations = 100000
    for i in tqdm(range(iterations)):
        grad_0 = calculate_grad_0(
            norm_mileage_list, norm_price_list, pred_theta_0, pred_theta_1
        )
        grad_1 = calculate_grad_1(
            norm_mileage_list, norm_price_list, pred_theta_0, pred_theta_1
        )
        pred_theta_0 = pred_theta_0 - learning_rate * grad_0
        pred_theta_1 = pred_theta_1 - learning_rate * grad_1
        cost = calculate_cost_func(
            norm_mileage_list, norm_price_list, pred_theta_0, pred_theta_1
        )
        if cost < threshold:
            break

    # Plot result
    fig = plt.figure(figsize=(16, 9))
    graph = fig.add_subplot(121)
    norm_graph = fig.add_subplot(122)

    normalized_point_0 = np.array([0, pred_theta_0])
    normalized_point_1 = np.array([(-1) * pred_theta_0 / pred_theta_1, 0])
    norm_line_x = np.array([normalized_point_0[0], normalized_point_1[0]])
    norm_line_y = np.array([normalized_point_0[1], normalized_point_1[1]])
    norm_graph.plot(norm_line_x, norm_line_y, color="red")

    norm_graph.plot(norm_mileage_list, norm_price_list, "bo")
    norm_graph.axis([0, max(norm_mileage_list) + 0.1, 0, max(norm_price_list) + 0.1])
    norm_graph.set_xlabel("Mileage[km]")
    norm_graph.set_ylabel("Price[USD]")
    norm_graph.set_title("Normalized result")

    reversed_point_0_x = reverse_before_normalization(
        normalized_point_0[0], mileage_list
    )
    reversed_point_0_y = reverse_before_normalization(normalized_point_0[1], price_list)
    reversed_point_1_x = reverse_before_normalization(
        normalized_point_1[0], mileage_list
    )
    reversed_point_1_y = reverse_before_normalization(normalized_point_1[1], price_list)
    final_pred_theta_1 = (reversed_point_0_y - reversed_point_1_y) / (
        reversed_point_0_x - reversed_point_1_x
    )
    final_pred_theta_0 = reversed_point_0_y - final_pred_theta_1 * reversed_point_0_x

    point_0 = np.array([0, final_pred_theta_0])
    point_1 = np.array([(-1) * final_pred_theta_0 / final_pred_theta_1, 0])
    line_x = np.array([point_0[0], point_1[0]])
    line_y = np.array([point_0[1], point_1[1]])
    graph.plot(line_x, line_y, color="red")

    graph.plot(mileage_list, price_list, "bo")
    graph.axis([0, max(mileage_list) + 10000, 0, max(price_list) + 1000])
    graph.set_xlabel("Mileage[km]")
    graph.set_ylabel("Price[USD]")
    graph.set_title("Final result")

    print("The number of iterations: ", i + 1)
    print("Final cost: ", cost)
    print("final_pred_theta_0: ", final_pred_theta_0)
    print("final_pred_theta_1: ", final_pred_theta_1)

    save_parameter(final_pred_theta_0, final_pred_theta_1, output_param_path)

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv_file_path")
    parser.add_argument("--output_param_path")
    args = parser.parse_args()
    train(args.csv_file_path, args.output_param_path)
