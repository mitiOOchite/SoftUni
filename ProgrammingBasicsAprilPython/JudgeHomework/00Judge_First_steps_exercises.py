#7 # # name = input()
# # # last_name = input()
# # # age = input()
# # # city = input()
# # # print(f"You are {name} {last_name}, a {age}-years old person from {city}.")

#8 # architect_name = input()
# # project_count = int(input())
# # project_time = project_count*3
# # print(f"The architect {architect_name} will need {project_time} hours to complete {project_count} project/s.")

#9 dog_food_price = 2.50
# cat_food_price = 4
# dog_food_quantity = int(input())
# cat_food_quantity = int(input())
# total_food_price= cat_food_price * cat_food_quantity + dog_food_price*dog_food_quantity
# print(f"{total_food_price} lv.")

# price_per_sqm = 7.61
# greaning_meters = int(input())
# price = (greaning_meters*price_per_sqm)
# discount = price*0.18
# price_after_discount = price -(discount)
# print(f"The final price is: {price_after_discount} lv.")
# print(f"The discount is: {discount} lv.")

number_one = float(input())
number_two = float(input())
convert = number_one*60
final_num = convert-number_two
final_num2 = final_num//60
print(f"{final_num2:.02f},{final_num:.02f}")