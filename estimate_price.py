import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mileage')
    args = parser.parse_args()
    print(args.mileage)
    # main(args.mileage)
