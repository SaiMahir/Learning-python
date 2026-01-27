import random
l = list(map(int,input("enter elements:").split()))
for i in range (5):
    a  = random.choice(l)
    print("random element is :", a)