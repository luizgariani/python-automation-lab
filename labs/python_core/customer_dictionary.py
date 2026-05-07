customer = {
    "name": "Maria Silva",
    "email": "maria@email.com",
    "cpf": "00000000000"
}

order = {
    "id": "BR123456",
    "status": "shipped",
    "tracking_code": "PX987654321BR"
}

print("Customer support summary")
print("------------------------")
print(f"Customer: {customer['name']}")
print(f"Email: {customer['email']}")
print(f"CPF: {customer['cpf']}")
print(f"Order ID: {order['id']}")
print(f"Status: {order['status']}")
print(f"Tracking code: {order['tracking_code']}")