import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_file_path')
    args = parser.parse_args()
    print(args.csv_file_path)
    # main(args.csv_file_path)
