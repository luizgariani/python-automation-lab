import json
from pathlib import Path
from typing import Optional


Order = dict[str, Optional[str]]


def load_orders(file_path: Path) -> list[Order]:
    """Load order records from a JSON file."""
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def print_order_summary(order: Order) -> None:
    """Print a short summary for a single order."""
    customer_name = order.get("customer_name") or "Customer"
    order_id = order.get("order_id") or "unknown"
    status = order.get("status") or "unknown"
    tracking_code = order.get("tracking_code") or "not available"

    print(f"Customer: {customer_name}")
    print(f"Order ID: {order_id}")
    print(f"Status: {status}")
    print(f"Tracking code: {tracking_code}")
    print("-----------------------")


def main() -> None:
    """Read orders from JSON and print their summaries."""
    current_dir = Path(__file__).parent
    orders_file = current_dir / "orders.json"

    orders = load_orders(orders_file)

    print("Orders loaded from JSON")
    print("-----------------------")

    for order in orders:
        print_order_summary(order)


if __name__ == "__main__":
    main()