from typing import Callable, Optional


Order = dict[str, Optional[str]]
StatusMessageHandler = Callable[[Order], str]


def get_customer_name(order: Order) -> str:
    """Return the customer name or a default value when it is missing."""
    return order.get("customer_name") or "Customer"


def get_order_id(order: Order) -> str:
    """Return the order ID or a default value when it is missing."""
    return order.get("order_id") or "unknown"


def message_shipped(order: Order) -> str:
    """Generate a support message for shipped orders."""
    customer_name = get_customer_name(order)
    order_id = get_order_id(order)
    tracking_code = order.get("tracking_code") or "not available"

    return (
        f"Hi {customer_name}, your order {order_id} has been shipped. "
        f"Tracking code: {tracking_code}."
    )


def message_processing(order: Order) -> str:
    """Generate a support message for orders still being processed."""
    customer_name = get_customer_name(order)
    order_id = get_order_id(order)

    return (
        f"Hi {customer_name}, your order {order_id} is still being processed. "
        "The tracking code is not available yet."
    )


def message_delivered(order: Order) -> str:
    """Generate a support message for delivered orders."""
    customer_name = get_customer_name(order)
    order_id = get_order_id(order)

    return f"Hi {customer_name}, your order {order_id} has already been delivered."


def message_canceled(order: Order) -> str:
    """Generate a support message for canceled orders."""
    customer_name = get_customer_name(order)
    order_id = get_order_id(order)

    return (
        f"Hi {customer_name}, your order {order_id} was canceled. "
        "Please contact support if you need more details."
    )


def message_unknown(order: Order) -> str:
    """Generate a fallback message when the order status is unknown."""
    customer_name = get_customer_name(order)
    order_id = get_order_id(order)

    return (
        f"Hi {customer_name}, we could not identify the current status "
        f"of your order {order_id}."
    )


STATUS_HANDLERS: dict[str, StatusMessageHandler] = {
    "shipped": message_shipped,
    "processing": message_processing,
    "delivered": message_delivered,
    "canceled": message_canceled,
}


def generate_order_status_message(order: Order) -> str:
    """Generate a customer-friendly message based on the order status."""
    status = order.get("status") or "unknown"
    handler = STATUS_HANDLERS.get(status, message_unknown)

    return handler(order)