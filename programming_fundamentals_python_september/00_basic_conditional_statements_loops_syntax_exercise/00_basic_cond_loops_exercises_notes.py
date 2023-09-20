# # # Lecture notes
# # range(start,stop,step)
# # def __init__(self, stop: SupportsIndex) -> None
# # range(stop) -> range object range(start, stop[, step]) -> range object
# # Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.
# # range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3.
# # These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).
# #
# # lower()
# # upper()
# name ='AnatoLi'
# print(name.lower())
# print(name.upper())
#string index [0] square brackets, if we want part of it same as range we have [start:stop:step]
some_string = 'Hello!'
print(len(some_string))
print(some_string[::-1])