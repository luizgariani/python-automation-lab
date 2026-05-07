def generate_order_status_message(order):
    customer_name = order.get("customer_name", "Customer")
    order_id = order.get("order_id", "unknown")
    status = order.get("status", "unknown")
    tracking_code = order.get("tracking_code")

    if status == "shipped":
        return (
            f"Hi {customer_name}, your order {order_id} has been shipped. "
            f"Tracking code: {tracking_code}."
        )

    if status == "processing":
        return (
            f"Hi {customer_name}, your order {order_id} is still being processed. "
            "The tracking code is not available yet."
        )

    if status == "delivered":
        return f"Hi {customer_name}, your order {order_id} has already been delivered."

    if status == "canceled":
        return (
            f"Hi {customer_name}, your order {order_id} was canceled. "
            "Please contact support if you need more details."
        )

    return (
        f"Hi {customer_name}, we could not identify the current status "
        f"of your order {order_id}."
    )