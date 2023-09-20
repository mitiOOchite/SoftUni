#1 Excellent score

# grade = float(input())
# if grade >= 5.50:
#     print("Excellent!")

#2 Greater Number

# first_num = int(input())
# second_num = int(input())
#
# if first_num >= second_num:
#     print(first_num)
# else:
#     print(second_num)

#3 Odd or even

# number = int(input())
#
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

#4 Password guess
# CORRECT_PASSWORD = "s3cr3t!P@ssw0rd"
# user_password = input()
# if user_password == CORRECT_PASSWORD:
#     print("Welcome")
# else:
#     print("Wrong password!")

#5 num between 100 and 200

# UPPER_RANGE = 200
# LOWER_RANGE = 100
# number = int(input())
#
# if number < LOWER_RANGE:
#     print(f"Less than {LOWER_RANGE}")
# elif number >= LOWER_RANGE and number <= UPPER_RANGE:
#     print(f"Between {LOWER_RANGE} and {UPPER_RANGE}")
# else:
#     print(f"Greater than {UPPER_RANGE}")

#5 Speed info

# SLOW = 10
# AVERAGE = 50
# FAST = 150
# ULTRA_FAST = 1000
# speed = float(input())
#
# if speed <= SLOW:
#     print("slow")
# elif SLOW <= speed <= AVERAGE:
#     print("average")
# elif AVERAGE <= speed <= FAST:
#     print("fast")
# elif FAST <= speed <= ULTRA_FAST:
#     print("ultra fast")
# else:
#     print("extremely fast")

#6 Area of figure
# import math
#
# type_of_figure = input()
# area = 0#if we dont add the initial area variable, once none of the conditions is met, we will not have a value for area resulting in an error
# if type_of_figure == "rectangle":
#     side_a = float(input())
#     side_b = float(input())
#     area = side_b*side_a
# elif type_of_figure == "circle":
#     radius = float(input())
#     area = math.pi*(radius**2)
# elif type_of_figure == "triangle":
#     length = float(input())
#     height = float(input())
#     area = length*height/2
# elif type_of_figure == "square":
#     length = float(input())
#     area = length**2
# print(f"{area:.3f}")