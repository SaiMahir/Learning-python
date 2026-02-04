"""#The filter() function is used to filter elements from an iterable based on a specified condition.

lst = map(int, input("enter numbers :").split( ))
even_numbers = filter(lambda x: x % 2 == 0, lst)
print("Even numbers are:", list(even_numbers))"""

#The reduce() function is used to apply a function cumulatively to the elements of an iterable and reduce it to a single value.

from functools import reduce

numbers  = map (int, input("enter numbers: ").split())
product = reduce(lambda a, b: a * b, numbers)
print(product)


