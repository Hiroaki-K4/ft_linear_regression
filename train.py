import argparse
import visualize_data


def calculate_cost_func(mileage_list, price_list, pred_theta_0, pred_theta_1):
    diff_sum = 0
    for i in range(len(mileage_list)):
        diff_sum += (price_list[i] - (pred_theta_1 * mileage_list[i] + pred_theta_0)) ** 2

    return diff_sum / len(mileage_list)


def calculate_grad_0(mileage_list, price_list, pred_theta_0, pred_theta_1):
    diff_sum = 0
    for i in range(len(mileage_list)):
        diff_sum += price_list[i] - (pred_theta_1 * mileage_list[i] + pred_theta_0)

    print("i: ", i)
    print("len: ", (-2) * diff_sum / len(mileage_list))
    return (-2) * diff_sum / len(mileage_list)


def calculate_grad_1(mileage_list, price_list, pred_theta_0, pred_theta_1):
    diff_sum = 0
    for i in range(len(mileage_list)):
        diff_sum += mileage_list[i] * (price_list[i] - (pred_theta_1 * mileage_list[i] + pred_theta_0))

    return (-2) * diff_sum / len(mileage_list)


def train(csv_file_path: str, output_param_path: str):
    print(csv_file_path)
    print(output_param_path)
    init_theta_0 = 0
    init_theta_1 = 0
    learning_rate = 0.000001
    threshold = 0.0001

    mileage_list, price_list = visualize_data.read_data(csv_file_path)
    print(mileage_list, price_list)
    pred_theta_0 = init_theta_0
    pred_theta_1 = init_theta_1
    old_cost = calculate_cost_func(mileage_list, price_list, pred_theta_0, pred_theta_1)
    iterations = 10000
    for i in range(iterations):
        grad_0 = calculate_grad_0(mileage_list, price_list, pred_theta_0, pred_theta_1)
        grad_1 = calculate_grad_1(mileage_list, price_list, pred_theta_0, pred_theta_1)
        print("grad_0: ", grad_0)
        print("grad_1: ", grad_1)
        pred_theta_0 = pred_theta_0 - learning_rate * grad_0
        pred_theta_1 = pred_theta_1 - learning_rate * grad_1
        cost = calculate_cost_func(mileage_list, price_list, pred_theta_0, pred_theta_1)
        if abs(old_cost - cost) < threshold:
            print("Diff is too small.")
            break
        print("cost: ", cost)
        old_cost = cost


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_file_path')
    parser.add_argument('--output_param_path')
    args = parser.parse_args()
    train(args.csv_file_path, args.output_param_path)
