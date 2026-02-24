s = {1,2,3}
s1 = {3,4,5}
u = s.union(s1)
print("Union of sets:", u)
i = s.intersection(s1)
print("Intersection of sets:", i)
d = s.difference(s1)
print("Difference of sets (s - s1):", d)
sym_diff = s.symmetric_difference(s1)
print("Symmetric Difference of sets:", sym_diff)
# Checking subset and superset
sub = s.issubset(s1)
print("Is s a subset of s1?:", sub)
sup = s1.issuperset(s)
print("Is s1 a superset of s?:", sup)
p = s.remove(2)
print("Set after removing element 2:", s)
s.add(6)
print("Set after adding element 6:", s)
s.clear()
print("Set after clearing all elements:", s)
# Copying a set
s_copy = s1.copy()
print("Copy of s1:", s_copy)

