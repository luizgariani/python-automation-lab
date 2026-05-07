def generate_order_status_message(order):
    customer_name = order["customer_name"]
    order_id = order["order_id"]
    status = order["status"]
    tracking_code = order["tracking_code"]

    if status == "shipped":
        return (
            f"Hi {customer_name}, your order {order_id} has been shipped. "
            f"Tracking code: {tracking_code}."
        )

    elif status == "processing":
        return (
            f"Hi {customer_name}, your order {order_id} is still being processed. "
            "The tracking code is not available yet."
        )

    elif status == "delivered":
        return (
            f"Hi {customer_name}, your order {order_id} has already been delivered."
        )

    elif status == "canceled":
        return (
            f"Hi {customer_name}, your order {order_id} was canceled. "
            "Please contact support if you need more details."
        )

    else:
        return (
            f"Hi {customer_name}, we could not identify the current status "
            f"of your order {order_id}."
        )


orders = [
    {
        "customer_name": "Maria Silva",
        "order_id": "BR123456",
        "status": "shipped",
        "tracking_code": "PX987654321BR"
    },
    {
        "customer_name": "João Santos",
        "order_id": "BR654321",
        "status": "processing",
        "tracking_code": None
    },
    {
        "customer_name": "Ana Oliveira",
        "order_id": "BR789123",
        "status": "delivered",
        "tracking_code": "PX123456789BR"
    },
    {
        "customer_name": "Carlos Lima",
        "order_id": "BR000999",
        "status": "canceled",
        "tracking_code": None
    }
]

print("Generated support messages")
print("--------------------------")

for order in orders:
    message = generate_order_status_message(order)
    print(message)
    print("--------------------------")