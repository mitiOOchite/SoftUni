# 1 Sum Seconds
# seconds_first = int(input())
# seconds_second = int(input())
# seconds_third = int(input())
#
# seconds_sum = seconds_first + seconds_second + seconds_third
# # print(seconds_sum)
# time_minutes = seconds_sum // 60
# time_seconds = seconds_sum % 60
# if time_seconds < 10:
#     print(f"{time_minutes}:{time_seconds:02d}")
# else:
#     print(f"{time_minutes}:{time_seconds}")

# 2 Bonus Points
# starting_number = int(input())
# bonus_points = 0
# if starting_number <= 100:
#     bonus_points = 5
#     #bonus_points += 5 (adds 5 when called)
# elif starting_number <= 1000:
#     bonus_points = starting_number * 0.2
# elif starting_number > 1000:
#     bonus_points = starting_number * 0.1
#
# bonus_extra_points = 0
# if starting_number % 2 == 0:
# #     bonus_extra_points = 1
# # elif starting_number % 10 == 5:
# #     bonus_extra_points = 2
# # print(bonus_points+bonus_extra_points)
# # print(bonus_points+bonus_extra_points+starting_number)

# 3 Time + 15
ADDED_MINUTES = 45
hours = int(input())
minutes = int(input())

convert_hours = hours * 60 #to convert everything in minutes
hours_and_minutes = convert_hours + minutes - ADDED_MINUTES
# print(hours_and_minutes)
hours_of_time = hours_and_minutes // 60 #to get the hours of the time division without remainder
minutes_remainder = hours_and_minutes % 60# to get the minutes part of the time
# print(f"{hours_of_time}:{minutes_remainder}")
if hours_of_time > 23:
    new_hour = 0
else:
    new_hour = hours_of_time
print(f"{new_hour}:{minutes_remainder:02d}")

#4 Godzilla vs KONG

# decor  = 10% from the budget) 0.1*budget
# discount = when more than 150 statists , clothing discount 10% from total clothing price?

# budget = float(input())
# statists_count = int(input())
# price_per_costume = float(input())
# total_price = statists_count*price_per_costume
# decor = 0.1 * budget
#
# if statists_count > 150:
#     total_price = total_price-(0.1*total_price)
# else:
#     total_price
#
# final_price = total_price+decor
# budget_diff = abs(budget - final_price) #absolute returns the positive number
# if final_price > budget:
#     print("Not enough money!")
#     print(f"Wingard needs {budget_diff:.02f} leva more.")
# else:
#     print("Action!")
#     print(f"Wingard starts filming with {budget_diff:.02f} leva left.")

#5 World Record
# METERS_DELAY = 15
# SECONDS_DELAY = 12.5
# current_record = float(input())
# distance_in_meters = float(input())
# seconds_per_meter = float(input())
# #delay = distance_in_meters//15 = result * 12.5
# # calc time in seconds for which the distance will be traveled and the diff with the world record
# delay = (distance_in_meters//METERS_DELAY)*SECONDS_DELAY
# total_time = (distance_in_meters*seconds_per_meter)+delay
# time_diff = abs(current_record - total_time)
# if total_time < current_record:
#     print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
# else:
#     print(f"No, he failed! He was {time_diff:.2f} seconds slower.")

#6 Shopping

#discount = if gpu_count > cpu_count - 15% off total price
#cpu_price = 35% from the price of the bought gpus
#ram = 10% from the price of the bough gpu
#
# PRICE_PER_GPU = 250
# budget = float(input())
# gpu_count = int(input())
# cpu_count = int(input())
# ram_count = int(input())
# gpu_price = PRICE_PER_GPU*gpu_count
# cpu_price = 0.35*gpu_price
# ram_price = 0.10*gpu_price
#
# final_price = cpu_price*cpu_count+gpu_price+ram_price*ram_count
#
# if gpu_count > cpu_count:
#     final_price = final_price-(0.15*final_price)
# else:
#     final_price
#
# budget_diff = abs(final_price-budget)
#
# if final_price <= budget:
#     print(f"You have {budget_diff:.2f} leva left!")
# else:
#     print(f"Not enough money! You need {budget_diff:.2f} leva more!")

#7 Lunch break
# from math import ceil
# series_name = str(input())
# series_time = int(input())
# breaktime = int(input())
#
# lunch_time = 0.125*breaktime
# print(lunch_time)
# time_off = 0.25*breaktime
# print(time_off)
# time_left = breaktime - lunch_time - time_off
# print(time_left)
#
# final_time_left = abs(time_left - series_time)
#
# if time_left >= series_time:
#     print(f"You have enough time to watch {series_name} and left with {ceil(final_time_left)} minutes free time.")
# else:
#     print(f"You don't have enough time to watch {series_name}, you need {ceil(final_time_left)} more minutes.")