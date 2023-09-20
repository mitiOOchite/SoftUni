month = input()  # - May, June, July, August, September,October
number_of_nights = int(input())
# За студио, при повече от 7 нощувки през май и октомври : 5% намаление. 0.95 from price
# За студио, при повече от 14 нощувки през май и октомври : 30% намаление. 0.70 from price
# За студио, при повече от 14 нощувки през юни и септември: 20% намаление. 0.80 fom price
# За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление

studio_price_per_night = 0
apartment_price_per_night = 0
if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 14 >= number_of_nights > 7:
        studio_price_per_night *= 0.98
    elif number_of_nights > 14:
        studio_price_per_night *= 0.70
elif month == "June" or month == "September":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if number_of_nights > 14:
        studio_price_per_night *= 0.80
elif month == "July" or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77

if number_of_nights > 14:
    apartment_price_per_night *= 0.90

total_apartment_cost = number_of_nights * apartment_price_per_night
total_studio_cost = number_of_nights * studio_price_per_night

print(f"Apartment : {total_apartment_cost:.2f}")
print(f"Studio: {total_studio_cost:.2f}")
