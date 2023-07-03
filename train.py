import argparse


def train(csv_file_path: str, output_param_path: str):
    print(csv_file_path)
    print(output_param_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_file_path')
    parser.add_argument('--output_param_path')
    args = parser.parse_args()
    train(args.csv_file_path, args.output_param_path)
