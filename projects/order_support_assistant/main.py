from data import orders
from messages import Order, generate_order_status_message


def print_separator() -> None:
    """Print a visual separator for terminal output."""
    print("-----------------------")


def print_header() -> None:
    """Print the application header."""
    print("Order Support Assistant")
    print_separator()


def process_orders(order_list: list[Order]) -> None:
    """Process orders and print the generated support messages."""
    for order in order_list:
        message = generate_order_status_message(order)
        print(message)
        print_separator()


def main() -> None:
    """Run the Order Support Assistant flow."""
    print_header()
    process_orders(orders)


if __name__ == "__main__":
    main()