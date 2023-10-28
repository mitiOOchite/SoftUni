class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        # self._brand = brand private attr
        # self.__brand = brand protected attr
        self.model = model
        self.year = year


car1 = Car('Mercedes', 190, 1995)
print(car1.__dict__)
print(car1.brand, car1.year, car1.model)
car1.brand = 'BMW'
print(car1.brand)
# car1 = ['BrandL Mercedes', 'Model:190', 'Year:1995']
# car2 = ['BrandL Mercedes', 'Model:124', 'Year:1995']
