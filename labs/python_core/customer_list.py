customers = [
    {
        "name": "Maria Silva",
        "email": "maria@email.com",
        "cpf": "00000000000",
        "order_id": "BR123456",
        "order_status": "shipped",
        "tracking_code": "PX987654321BR"
    },
    {
        "name": "João Santos",
        "email": "joao@email.com",
        "cpf": "11111111111",
        "order_id": "BR654321",
        "order_status": "processing",
        "tracking_code": None
    },
    {
        "name": "Ana Oliveira",
        "email": "ana@email.com",
        "cpf": "22222222222",
        "order_id": "BR789123",
        "order_status": "delivered",
        "tracking_code": "PX123456789BR"
    }
]

print("Customer support summaries")
print("--------------------------")

for customer in customers:
    print(f"Customer: {customer['name']}")
    print(f"Email: {customer['email']}")
    print(f"CPF: {customer['cpf']}")
    print(f"Order ID: {customer['order_id']}")
    print(f"Status: {customer['order_status']}")
    print(f"Tracking code: {customer['tracking_code']}")
    print("--------------------------")