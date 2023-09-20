import math

type_of_figure = input()
area = 0#if we dont add the initial area variable, once none of the conditions is met, we will not have a value for area resulting in an error
if type_of_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_b*side_a
elif type_of_figure == "circle":
    radius = float(input())
    area = math.pi*(radius**2)
elif type_of_figure == "triangle":
    length = float(input())
    height = float(input())
    area = length*height/2
elif type_of_figure == "square":
    length = float(input())
    area = length**2
print(f"{area:.3f}")