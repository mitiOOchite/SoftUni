number_of_orders = int(input())
total_price = 0
for order in range(0,number_of_orders):
    current_price = 0
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule >100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules <1 or capsules > 2000:
        continue
    else:
        current_price = price_per_capsule*days*capsules
        total_price += current_price
        print(f'The price for the coffee is: ${current_price:.2f}')
print(f'Total: ${total_price:.2f}')