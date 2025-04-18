#
#
# doubles = [x * 2 for x in range(1,11)]
# triples= [y* 3 for y in range(1,11)]
# squares = [z*z for z in range(1,11)]
#
# print(squares)
from sympy import print_glsl

# fruits = ["apple", "orange", "banana", "coconut"]
# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruit_chars)

# numbers = [1, -2, 3, -4, 5, -6]
# positive_nums = [ num for num in numbers if num >= 0]
# negative_nums = [ num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 ==0]
# odd_nums = [num for num in numbers if num % 2 ==1]
# print(odd_nums)

grades =[87,34,56,73,62, 20]
passing_grades = [ grade for grade in grades if grade >= 60]
print(grades)