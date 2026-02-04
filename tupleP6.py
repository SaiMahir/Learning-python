t = [(1,'none'),(2,1),(3,'none')]
for i in t:
    if type(i)==tuple:
        if 'none' in i:
            t.remove(i)
print(t)

t = [(1,'none'), (2,1), (3,'none')]
t = [i for i in t if 'none' not in i]
print(t)