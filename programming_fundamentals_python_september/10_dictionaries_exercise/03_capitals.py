countries = input().split(', ')
capitals = input().split(', ')
country_dict = {countries[index]:capitals[index]
                for index in range(len(countries))}
for country, city in country_dict.items():
    print(f'{country} -> {city}')
#
# countries = input().split(', ')
# capitals = input().split(', ')
# country_dict = {}
#
# for index in range(len(countries)):
#     country_dict[countries[index]] = capitals[index]
#
# print(country_dict)