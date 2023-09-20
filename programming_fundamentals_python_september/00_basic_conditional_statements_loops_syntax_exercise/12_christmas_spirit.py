quantity_of_decorations = int(input())
remaining_days = int(input())
ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17
total_points = 0
total_cost = 0
for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:# this needs to be first because if the day is the 22nd we need to increase the quantity in the begining
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += quantity_of_decorations * ornament_set_price
        total_points += ornament_set_points
    if current_day % 3 == 0:  # we use another if to check the same day again, as elif would not capture the 6th day/ 12th day/24th day
        total_cost += quantity_of_decorations * (tree_skirt_price + tree_garland_price)
        total_points += tree_skirt_points + tree_garland_points
    if current_day % 5 == 0:
        total_cost += quantity_of_decorations * tree_lights_price
        total_points += tree_lights_points
        if current_day % 3 == 0:
            total_points += 30
    if current_day % 10 == 0:
        total_points -= 20
        total_cost += tree_skirt_price + tree_lights_price + tree_garland_price
if remaining_days % 10 == 0:
    total_points -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_points}')