days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
plundered_amount = 0
percent_left = 0
for current_day in range(1, days + 1):
    plundered_amount += daily_plunder
    if current_day % 3 == 0:
        plundered_amount += (daily_plunder * 0.5)
    if current_day % 5 == 0:
        plundered_amount -= (plundered_amount * 0.3)
if plundered_amount >= expected_plunder:
    print(f'Ahoy! {plundered_amount:.2f} plunder gained.')
else:
    percent_left = (plundered_amount / expected_plunder) * 100
    print(f"Collected only {percent_left:.2f}% of the plunder.")

