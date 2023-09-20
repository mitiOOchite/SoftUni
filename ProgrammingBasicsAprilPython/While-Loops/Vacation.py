vacation_cost = float(input())
amount_available = float(input())
total_money = amount_available
total_days = 0
consecutive_spend_days = 0
while True:
    action = input()
    current_amount = float(input())
    total_days += 1
    if action == "spend":
        consecutive_spend_days +=1
        total_money -= current_amount
        if total_money <= 0:
            total_money = 0
        if consecutive_spend_days >= 5:
            break
    elif action == "save":
        consecutive_spend_days = 0
        total_money += current_amount
        if total_money >= vacation_cost:
            break
if total_money >= amount_available:
    print(f"You saved the money for {total_days}")
else:
    print("You cant save the money")
    print(total_days)