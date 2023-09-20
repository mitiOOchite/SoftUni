total_balance = 0
command = input()

while command != "NoMoreMoney":
    current_sum = float(command)
    if current_sum < 0:
        print("Invalid Operation")
        break
    print(f"Increase: {current_sum:.2f}")
    total_balance += current_sum
    command = input()
print(f"Total: {total_balance:.2f}")