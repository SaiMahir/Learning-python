'''n = [1,2,3,4,5]
d= {}
for i in n:
    d[i] = i**2
print("Dictionary:", d)'''

'''l = [1,2,3,4,5]
l1 = [2,3,4,5,6]
d = {}
n = min(len(l), len(l1))
for i in range(n):
    d[l[i]] = l1[i]
res = {i: j for i, j in zip(l, l1)}

print("Dictionary:", res)'''

'''sentence = input("Enter a sentence: ")

words = sentence.split()
word_length = {}

for word in words:
    word_length[word] = len(word)

print("Dictionary of word lengths:", word_length)'''

'''fruits = {
    "apple": 120,"banana": 40,"mango": 80,"grapes": 45,"orange": 60}

a = {}
for i, j in fruits.items():
    if j > 50:
        a[i] = j
print(a)'''

l = [1,2,3,4,5]
d = {}
for i in l:
    if i % 2 == 0:
        d[i] = 'Even'
    else:
        d[i] = 'Odd'
print("Dictionary:", d)


        


    