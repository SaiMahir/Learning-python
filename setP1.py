l = [1,2,3,4,5,6,1,2,2,3,4]
l1 = [9,10,1,2,3,4,5,9,5,2,1]
l_set = set(l)
l1_set = set(l1)
set_union = l_set.union(l1_set)
print(list(set_union))