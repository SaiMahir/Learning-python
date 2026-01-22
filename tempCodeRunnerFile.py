from functools import reduce

numbers  = map (int, input("enter numbers: ").split())
product = reduce(lambda a, b: a * b, numbers)
print(product)