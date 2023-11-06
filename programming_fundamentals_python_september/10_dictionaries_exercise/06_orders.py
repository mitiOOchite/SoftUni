command = input()
product_dict = {}
while command != 'buy':
    product, price, quantity = command.split()
    if product in product_dict:
        product_dict[product][0] += float(quantity)
        product_dict[product][1] = float(price)
    else:
        product_dict[product] = [float(quantity), float(price)]
    command = input()
for key, value in product_dict.items():
    total_price = value[0] * value[1]
    print(f'{key} -> {total_price:.2f}')
