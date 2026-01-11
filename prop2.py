def Sum(n, t):
    num = len(n)
    for i in range(num):
        for j in range(i + 1, num):
            if n[i] + n[j] == t:
                return [i, j]
    return None

n = list(map(int, input("Enter elements: ").split()))

t = int(input("Enter target sum: "))

result = Sum(n, t)
print(result)

