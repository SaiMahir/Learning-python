a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic Operators
print("\nArithmetic Operators")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

# Relational (Comparison) Operators
print("\nRelational Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical Operators
print("\nLogical Operators")
print("a > 0 and b > 0 :", a > 0 and b > 0)
print("a > 0 or b > 0  :", a > 0 or b > 0)
print("not(a > 0)     :", not(a > 0))

# Assignment Operators
print("\nAssignment Operators")
c = a
c += b
print("c += b ->", c)
c -= b
print("c -= b ->", c)
c *= b
print("c *= b ->", c)
c /= b
print("c /= b ->", c)

# Bitwise Operators
print("\nBitwise Operators")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
