products = {}

while True:
    input_data = input()
    if input_data == "buy":
        break

    product_info = input_data.split()
    name, price, quantity = product_info[0], float(product_info[1]), int(product_info[2])

    if name in products:
        products[name]['price'] = price
        products[name]['quantity'] += quantity
    else:
        products[name] = {'price': price, 'quantity': quantity}

for product, data in products.items():
    total_price = data['price'] * data['quantity']
    print(f"{product} -> {total_price:.2f}")