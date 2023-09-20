from math import ceil
gpu_count = 13
prehodnik_count = 13
remaining_parts_price = 1000
gpu_price = int(input())
prehodnik_price = int(input())
electricity_consumption = float(input())
profit_per_day = float(input())

total_assembly_price = gpu_price*gpu_count+prehodnik_price*prehodnik_count+remaining_parts_price
daily_win = profit_per_day-electricity_consumption
total_daily_win = gpu_count*daily_win
days_to_win_back_money = ceil(total_assembly_price/total_daily_win)
print(total_assembly_price)
print(days_to_win_back_money)
