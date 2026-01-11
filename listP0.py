n = int(input("Enter the number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input("Enter element: ")))

def prime_numbers(lst):
    primes = []
    for num in lst:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

def armstrong_numbers(lst):
    armstrongs = []
    for num in lst:
        order = len(str(num))
        sum_of_powers = sum(int(digit) ** order for digit in str(num))
        if num == sum_of_powers:
            armstrongs.append(num)
    return armstrongs

def perfect_numbers(lst):
    perfects = []
    for num in lst:
        if num > 1:
            divisors_sum = sum(i for i in range(1, num) if num % i == 0)
            if divisors_sum == num:
                perfects.append(num)
    return perfects

def neon_numbers(lst):
    neons = []
    for num in lst:
        square = num ** 2
        digit_sum = sum(int(digit) for digit in str(square))
        if digit_sum == num:
            neons.append(num)
    return neons    

check = int(input("Enter 1 for Prime, 2 for Armstrong, 3 for Perfect, 4 for Neon: "))

if check == 1:
    result = prime_numbers(lst)
    print("Prime numbers in the list:", result)
elif check == 2:
    result = armstrong_numbers(lst)
    print("Armstrong numbers in the list:", result)
elif check == 3:
    result = perfect_numbers(lst)
    print("Perfect numbers in the list:", result)
elif check == 4:
    result = neon_numbers(lst)
    print("Neon numbers in the list:", result)