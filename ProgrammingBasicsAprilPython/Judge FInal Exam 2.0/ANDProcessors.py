from math import floor
time_to_produce_CPU = 3
working_hours = 8
needed_cpu = int(input())
workers_count = int(input())
working_days = int(input())
cpu_price = 110.10
total_working_hours = workers_count*working_hours*working_days
cpus_made = floor(total_working_hours/time_to_produce_CPU)
total_money = abs(needed_cpu-cpus_made)*cpu_price
if cpus_made >= needed_cpu:
    print(f"Profit: -> {total_money:.2f} BGN")
if cpus_made < needed_cpu:
    print(f"Losses: -> {total_money:.2f} BGN")
