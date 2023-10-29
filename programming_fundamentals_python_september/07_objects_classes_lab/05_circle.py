class Circle:
    __pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter/2
    def calculate_circumference(self):
        circumference = 2*Circle.__pi*self.radius
        return circumference

    def calculate_area(self):
        area = Circle.__pi*self.radius**2
        return area
    def calculate_area_of_sector(self, angle):
       area_of_sector = (angle/360)*self.radius**2*Circle.__pi
       return area_of_sector

circle = Circle(int(input()))
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
