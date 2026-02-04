#List comprehension is a concise and readable way to create lists in Python using a single line of code instead of writing long loops.
"""lst = [i*i for i in range (1,11) ]
lst1 = [i for i in range (1,11) if i%2!= 0]
lst2 = [i*i for i in range (1,11)]

print(lst)
print(lst1)
print(lst2)
"""

celcius = [0,10,20,34.5]
farenheit = [(9/5)*i+32 for i in celcius]
print(farenheit)