#nested if
# if condition:
#     pass
#     if condition2:
#     pass
#     if condition3:
#     pass
# elif condition:
#     pass
ROSES_PRICE = 5
Dahlias_PRICE = 3.80
Tulips_PRICE = 2.80
Narcissus_PRICE = 3
Gladiolus_PRICE = 2.50

flower_type = input() #"Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
flower_quantity = int(input())
budget = int(input())

price = 0
discount = 0
if flower_type == "Roses":
    price = ROSES_PRICE
    if flower_quantity > 80:
        discount = 0.10
elif flower_type == "Dahlias":
    price = Dahlias_PRICE
    if flower_quantity > 90:
        discount = 0.15
elif flower_type == "Tulips":
    price = Tulips_PRICE
    if flower_quantity > 80:
        discount = 0.15
elif flower_type == "Narcissus":
    price = Narcissus_PRICE
    if flower_quantity < 120:
        discount = -0.15
elif flower_type == "Gladiolus":
    price = Gladiolus_PRICE
    if flower_quantity < 80:
        discount = -0.20
total_price = flower_quantity*price * (1 - discount)
if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_quantity} {flower_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")