def payload_for_create_product(name="svs", description="any", price=101, quantity=5):
    return {"name": name, "description": description, "price": price, "quantity": quantity}