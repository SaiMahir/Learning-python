l = list(map(int, input("Enter elements: ").split()))

for i in l:
    if i <= 1:
        print(i, "is not a prime")
        continue
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                print(i, "is not a prime")
                break
            else:
                print(i, "is prime")