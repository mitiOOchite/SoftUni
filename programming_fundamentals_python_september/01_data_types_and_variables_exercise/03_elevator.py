# number_of_people = int(input())
# capacity = int(input())
#
# courses =  number_of_people // capacity
#
# if number_of_people % capacity != 0:
#     courses += 1
# print(courses)
#
from math import ceil

number_of_people = int(input())
capacity = int(input())
courses = ceil(number_of_people / capacity)
print(courses)
