needed_eggs = 1
flour = 1
milk = 0.250
loaf_count = 0
current_eggs = 0
budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = (flour_price*1.25)/4
loaf_price = flour_price + eggs_price + milk_price
money_left = 0
lost_eggs = 0
while budget >= loaf_price:
    loaf_count += 1
    budget -= loaf_price
    current_eggs += 3
    if loaf_count % 3 == 0:
        lost_eggs = loaf_count-2
        if current_eggs - lost_eggs < 0: #make sure that eggs are never negative
            break
        else:
            current_eggs -= lost_eggs
print(f"You made {loaf_count} loaves of Easter bread! Now you have {current_eggs} eggs and {budget:.2f}BGN left.")
