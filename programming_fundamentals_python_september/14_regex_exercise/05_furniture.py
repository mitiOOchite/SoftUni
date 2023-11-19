import re

command = input()
bought_furniture = []
total_cost = 0
pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)'
while command != 'Purchase':
    items = re.findall(pattern, command)
    for item in items:
        bought_furniture.append(item[0])
        total_cost += float(item[1]) * int(item[2])
    command = input()
print('Bought furniture:')
for bought_item in bought_furniture:
    print(bought_item)
print(f'Total money spend: {total_cost:.2f}')
