from data import orders
from messages import generate_order_status_message


def main():
    print("Order Support Assistant")
    print("-----------------------")

    for order in orders:
        message = generate_order_status_message(order)
        print(message)
        print("-----------------------")


if __name__ == "__main__":
    main()