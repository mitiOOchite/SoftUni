change_amount = float(input())
coins_count = 0
pennies = int(change_amount * 100)#2.23 == 223
# [2lv == 200st, 1lv == 100st, 50st, 20st,10st, 5st, 2st,1st]

while pennies > 0:
    if pennies > 200:
        pennies -= 200
    elif pennies >= 100:
        pennies -= 100
    elif pennies >= 50:
        pennies -= 50
    elif pennies >= 20:
        pennies -= 20
    elif pennies >= 10:
        pennies -= 10
    elif pennies >= 5:
        pennies -= 5
    elif pennies >= 2:
        pennies -= 2
    elif pennies >= 1:
        pennies -= 1
    coins_count += 1

print(coins_count)
