
from math import ceil

min_km = 1000
training_days = int(input())
first_day_km = float(input())
total_km = 0
current_km = 0
for number in range(training_days+1):
    if number == 0:
        current_km = first_day_km
        total_km = current_km
    else:
        km_increase = int(input())/100
        total_km += (km_increase*current_km)+current_km
        current_km = (km_increase*current_km)+current_km
if total_km >= min_km:
    final_km = ceil(total_km-min_km)
    print(f"You've done a great job running {final_km} more kilometers!")
else:
    final_km = ceil(abs(total_km-min_km))
    print(f"Sorry Mrs. Ivanova, you need to run {final_km:} more kilometers")