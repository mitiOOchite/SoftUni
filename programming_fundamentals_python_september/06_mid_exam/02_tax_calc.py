vehicle = input().split(">>")
family_tax = 50
heavyDuty_tax = 80
sports_tax = 100
total_tax_paid = 0
valid_cars = ['family', 'heavyDuty','sports']
for current_car in vehicle:
    current_car_list = current_car.split()
    current_family_tax = family_tax
    current_heavy_tax = heavyDuty_tax
    current_sport_tax = sports_tax
    car_type = current_car_list[0]
    years_tax = int(current_car_list[1])
    km = int(current_car_list[2])
    if car_type not in valid_cars:
        print('Invalid car type.')
    elif car_type == 'family':
        current_family_tax -= 5*years_tax
        current_family_tax+= 12 * (km//3000)
        total_tax_paid+=current_family_tax
        print(f'A family car will pay {current_family_tax:.2f} euros in taxes.')
    elif car_type == 'heavyDuty':
        current_heavy_tax -= 8 * years_tax
        current_heavy_tax += 14 * (km // 9000)
        total_tax_paid += current_heavy_tax
        print(f'A heavyDuty car will pay {current_heavy_tax:.2f} euros in taxes.')
    elif car_type == 'sports':
        current_sport_tax -= 9 * years_tax
        current_sport_tax += 18 * (km // 2000)
        total_tax_paid += current_sport_tax
        print(f'A sports car will pay {current_sport_tax:.2f} euros in taxes.')
print(f'The National Revenue Agency will collect {total_tax_paid:.2f} euros in taxes.')