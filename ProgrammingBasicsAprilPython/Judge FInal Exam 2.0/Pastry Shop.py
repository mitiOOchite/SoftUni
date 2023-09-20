pastry = input()
amount_ordered = int(input())
day_of_order = int(input())
cake_price_until15 = 24
sufle_price_until15 = 6.66
baklavaprice_until15 = 12.60
cake_price_after = 28.70
sufle_price_after = 9.80
baklava_price_after = 16.98
discount_1 = 0.15
discount_2 = 0.25
discount_3_additional = 0.1
price = 0
final_price = 0
if pastry == "Cake" and day_of_order <= 15:
    price = cake_price_until15*amount_ordered
    if 100 <=  price <= 200:
        price = price - (price*discount_1)
    elif price > 200:
        price = price - (price*discount_2)
    final_price = price - (price *discount_3_additional)
elif pastry == "Cake" and day_of_order > 15:
    price = cake_price_after*amount_ordered
    if 100 <= price <= 200 and day_of_order <= 22:
        price = price - (price*discount_1)
    elif price > 200 and day_of_order <= 22:
        price = price - (price*discount_2)
    final_price = price
elif pastry == "Souffle" and day_of_order <= 15:
    price = sufle_price_until15*amount_ordered
    if 100<= price <= 200:
        price = price - (price*discount_1)
    elif price > 200:
        price = price - (price*discount_2)
    final_price = price - (price *discount_3_additional)
elif pastry == "Souffle" and day_of_order > 15:
    price = sufle_price_after*amount_ordered
    if 100<=  price <= 200 and day_of_order <=22:
        price = price - (price*discount_1)
    elif price > 200 and day_of_order <= 22:
        price = price - (price*discount_2)
    final_price = price
elif pastry == "Baklava" and day_of_order <= 15:
    price = baklavaprice_until15*amount_ordered
    if 100 <= price <= 200:
        price = price - (price*discount_1)
    elif price > 200:
        price = price - (price*discount_2)
    final_price = price - (price *discount_3_additional)
elif pastry == "Baklava" and day_of_order > 15:
    price = baklava_price_after*amount_ordered
    if 100 <= price <= 200 and day_of_order <= 22:
        price = price - (price*discount_1)
    elif price > 200 and day_of_order <= 22:
        price = price - (price*discount_2)
    final_price = price
print(f"{final_price:.2f}")
