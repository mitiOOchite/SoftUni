import re
string = input()
pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
items = re.findall(pattern,string)
sum_calories = 0
for item in items:
    product = item[1]
    date = item[2]
    calories = int(item[3])
    sum_calories += calories
days = sum_calories//2000
print(f'You have food to last you for: {days} days!')
for current_item in items:
    print(f'Item: {current_item[1]}, Best before: {current_item[2]}, Nutrition: {current_item[3]}')

# import re
# string = input()
# pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
# items = re.findall(pattern,string)
# sum_calories = sum(int(item[3]) for item in items)
# print(f'You have food to last you for: {sum_calories//2000} days!')
# for item in items:
#     product = item[1]
#     date = item[2]
#     calories = int(item[3])
#     print(f'Item: {product}, Best before: {date}, Nutrition: {calories}')
