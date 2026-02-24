d = {1:"apple", 2:"banana", 3:"cherry", 4:"date", 5:"elderberry"}
print("Keys:", d.keys())
print("Values:", d.values())
print("items:", d.items())
print("Dictionary:", d)
d[6] = "fig"
print('adding:', d[6])
d.update({7:"grape", 8:"honeydew"})
print("update:", d)
d.pop(2)
print("pop:", d)
