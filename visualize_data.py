import pandas as pd
import matplotlib.pyplot as plt


def visualize_data(csv_file_path: str):
    df = pd.read_csv(csv_file_path)
    mileage_list = df["km"].values.tolist()
    price_list = df["price"].values.tolist()
    print(mileage_list)
    print(price_list)
    data_list = []
    for i in range(len(mileage_list)):
        data_list.append([mileage_list[i], price_list[i]])

    print(data_list)

    plt.plot(mileage_list, price_list, 'bo')
    plt.axis([0, max(mileage_list)+10000, 0, max(price_list)+1000])
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.title("Relationship between the price of a car and mileage")
    plt.show()


if __name__ == '__main__':
    csv_file_path = "data.csv"
    visualize_data(csv_file_path)
