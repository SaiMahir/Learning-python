def check_number(n):
    temp = n

    # sum of digits & sum of even digits
    sum_digits = 0
    sum_even = 0
    while temp > 0:
        d = temp % 10
        sum_digits += d
        if d % 2 == 0:
            sum_even += d
        temp //= 10

    print("Sum of all digits:", sum_digits)
    print("Sum of even digits:", sum_even)

    # Neon number check
    sq = n * n
    neon_sum = 0
    while sq > 0:
        neon_sum += sq % 10
        sq //= 10
    if neon_sum == n:
        print("Neon number")
    else:
        print("Not a Neon number")

    # Harshad number check
    if sum_digits != 0 and n % sum_digits == 0:
        print("Harshad number")
    else:
        print("Not a Harshad number")

    # Armstrong number check
    temp = n
    digits = len(str(n))
    arm_sum = 0
    while temp > 0:
        d = temp % 10
        arm_sum += d ** digits
        temp //= 10
    if arm_sum == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

    # Prime number check
    if n <= 1:
        print("Not a Prime number")
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                print("Not a Prime number")
                break
        else:
            print("Prime number")


num = int(input("Enter a number: "))
check_number(num)
