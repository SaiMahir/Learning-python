from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

doc = Document()

# Title
title = doc.add_heading('Learning Python - Code Collection', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph('A comprehensive collection of Python programs covering fundamentals and best practices.')
doc.add_paragraph('By: Sai Mahir')
doc.add_paragraph()

# Table of Contents
doc.add_heading('Table of Contents', level=1)
toc = '''Section 1: Python Basics
    1.1 Syntax
    1.2 Variable - Integer
    1.3 Variable - Float
    1.4 Variable - String
    1.5 Variable - Boolean
    1.6 Multiple Assignment
    1.7 Typecasting

Section 2: Input and Output
    2.1 User Input
    2.2 Input Addition

Section 3: Strings and Math Functions
    3.1 String Methods
    3.2 Math Functions

Section 4: Operators
    4.1 All Operators
    4.2 Membership & Identity Operators

Section 5: Conditional Statements
    5.1 Positive/Negative Check
    5.2 Greatest Integer - Using If-Elif
    5.3 Greatest Integer - Using max()
    5.4 Grade Calculator
    5.5 Grade Calculator with Average

Section 6: Loops
    6.1 Print N Numbers with Even/Odd Count
    6.2 Fibonacci Series

Section 7: Practical Programs
    7.1 Swap Two Numbers
    7.2 Simple Interest
    7.3 Compound Interest
    7.4 Celsius to Fahrenheit
    7.5 Fahrenheit to Celsius
    7.6 Sum of First and Last Digit
    7.7 Number Length
    7.8 Sum of Even Digits

Section 8: Number Theory Programs
    8.1 Armstrong Number
    8.2 Neon Number
    8.3 Harshad Number
    8.4 Palindrome - Using While Loop
    8.5 Palindrome - Using String Slicing
'''
doc.add_paragraph(toc)
doc.add_page_break()

# ============== SECTION 1: BASICS ==============
doc.add_heading('Section 1: Python Basics', level=1)

# 1.1 Syntax
doc.add_heading('1.1 Syntax (syntax.py)', level=2)
doc.add_paragraph('Basic print statements - your first Python program.')
code = doc.add_paragraph()
code.add_run('''print("hello world")
print("i like pizza.")''').font.name = 'Consolas'

doc.add_paragraph()

# 1.2 Variable Integer
doc.add_heading('1.2 Variable - Integer (variableint.py)', level=2)
doc.add_paragraph('Working with integer variables and type checking.')
code = doc.add_paragraph()
code.add_run('''age = 18
age = 18 + 1
print(age) 
print("my age is "+ str(age))
print(type(age))''').font.name = 'Consolas'

doc.add_paragraph()

# 1.3 Variable Float
doc.add_heading('1.3 Variable - Float (variablefloat.py)', level=2)
doc.add_paragraph('Working with floating-point numbers.')
code = doc.add_paragraph()
code.add_run('''hight = 167.8
print(hight)
print("my hight is "+ str (hight))
print(type(hight))''').font.name = 'Consolas'

doc.add_paragraph()

# 1.4 Variable String
doc.add_heading('1.4 Variable - String (variablestring.py)', level=2)
doc.add_paragraph('Working with string variables and concatenation.')
code = doc.add_paragraph()
code.add_run('''name = 'Sai'
lastname = "mahir"
fullname = name + lastname
print(fullname)
print("my name is "+name)
print(type(name))''').font.name = 'Consolas'

doc.add_paragraph()

# 1.5 Variable Boolean
doc.add_heading('1.5 Variable - Boolean (variableboolean.py)', level=2)
doc.add_paragraph('Working with boolean (True/False) values.')
code = doc.add_paragraph()
code.add_run('''donkey = True
print(donkey)
print("are you a donkey: "+ str(donkey))
print(type(donkey))''').font.name = 'Consolas'

doc.add_paragraph()

# 1.6 Multiple Assignment
doc.add_heading('1.6 Multiple Assignment (multipleAssignment.py)', level=2)
doc.add_paragraph('Assigning multiple variables in one line.')
code = doc.add_paragraph()
code.add_run('''name,age,hight="sai",18,167.8
print(name)
print(age)
print(hight)

sai = mahir = 18
print(sai)''').font.name = 'Consolas'

doc.add_paragraph()

# 1.7 Typecasting
doc.add_heading('1.7 Typecasting (typecasting.py)', level=2)
doc.add_paragraph('Converting between different data types.')
code = doc.add_paragraph()
code.add_run('''a = 1
b = 2.5
c = "3"

a=float(a)
b=str(b)
c=int(c)

print(a)
print(b)
print(c)

print("value of x is"+b)
#typecasting is converting one data type to another data type.''').font.name = 'Consolas'

doc.add_paragraph()

# ============== SECTION 2: INPUT/OUTPUT ==============
doc.add_heading('Section 2: Input and Output', level=1)

# 2.1 Input
doc.add_heading('2.1 User Input (input.py)', level=2)
doc.add_paragraph('Taking input from the user.')
code = doc.add_paragraph()
code.add_run('''name = input("ENter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

age = str(age)
height = str(height)

print("hello "+name)
print("You are "+age+" years old.")
print("Your height is  "+height+" metrs.")''').font.name = 'Consolas'

doc.add_paragraph()

# 2.2 Input Addition
doc.add_heading('2.2 Input Addition (inputADD.py)', level=2)
doc.add_paragraph('Adding two numbers from user input.')
code = doc.add_paragraph()
code.add_run('''a = int(input("enter first number: "))
b = int(input("enter second number: "))

sum = a+b

print("the sum is: ",sum)''').font.name = 'Consolas'

doc.add_paragraph()

# ============== SECTION 3: STRING & MATH ==============
doc.add_heading('Section 3: Strings and Math Functions', level=1)

# 3.1 String Basics
doc.add_heading('3.1 String Methods (stringbasics.py)', level=2)
doc.add_paragraph('Common string methods and operations.')
code = doc.add_paragraph()
code.add_run('''name = 'sai'
print(len(name))
print(name[0])
print(name.find('i'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('o'))
print(name.replace('a','o'))
print(name *5)''').font.name = 'Consolas'

doc.add_paragraph()

# 3.2 Math Functions
doc.add_heading('3.2 Math Functions (mathfunc.py)', level=2)
doc.add_paragraph('Using the math module for mathematical operations.')
code = doc.add_paragraph()
code.add_run('''import math

pi = 3.14

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(pi))
print(math.log(pi))
print(max(1,2,3,4))
print(min(1,2,3,4))
print(math.sqrt(16))
print(math.factorial(5))
print(math.sin(90))
print(math.cos(0))
print(math.tan(45))
print(math.gcd(12,15))
print(math.lcm(12,15))
print(math.exp(2))
print(math.degrees(math.pi/2))
print(math.radians(90))''').font.name = 'Consolas'

doc.add_paragraph()

# ============== SECTION 4: OPERATORS ==============
doc.add_heading('Section 4: Operators', level=1)

# 4.1 Operators
doc.add_heading('4.1 All Operators (operators.py)', level=2)
doc.add_paragraph('Arithmetic, Relational, Logical, Assignment, and Bitwise operators.')
code = doc.add_paragraph()
code.add_run('''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic Operators
print("\\nArithmetic Operators")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

# Relational (Comparison) Operators
print("\\nRelational Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical Operators
print("\\nLogical Operators")
print("a > 0 and b > 0 :", a > 0 and b > 0)
print("a > 0 or b > 0  :", a > 0 or b > 0)
print("not(a > 0)     :", not(a > 0))

# Assignment Operators
print("\\nAssignment Operators")
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
print("\\nBitwise Operators")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)''').font.name = 'Consolas'

doc.add_paragraph()

# 4.2 Membership & Identity Operators
doc.add_heading('4.2 Membership & Identity Operators (operators[extra].py)', level=2)
doc.add_paragraph('Using in, not in, is, and is not operators.')
code = doc.add_paragraph()
code.add_run('''list1 = [10, 20, 30, 40]
str1 = "python"

a = 20
b = 20
c = list1
d = list1.copy()

# Membership Operators
print("Membership Operators")
print("20 in list1       :", 20 in list1)
print("50 not in list1   :", 50 not in list1)
print("'p' in str1       :", 'p' in str1)
print("'z' not in str1   :", 'z' not in str1)

# Identity Operators
print("\\nIdentity Operators")
print("a is b            :", a is b)
print("a is not b        :", a is not b)
print("c is d            :", c is d)
print("c is not d        :", c is not d)''').font.name = 'Consolas'

doc.add_paragraph()

# ============== SECTION 5: CONDITIONALS ==============
doc.add_heading('Section 5: Conditional Statements', level=1)

# 5.1 Positive/Negative
doc.add_heading('5.1 Positive/Negative Check (positiveNegitive.py)', level=2)
doc.add_paragraph('Checking if a number is positive, negative, or zero with nested conditions.')
code = doc.add_paragraph()
code.add_run('''a  = int (input("Enter a number: "))

if a > 0:
    print("Positive")
    if a%2==0:
        print("Even")
    else:
        print("Odd")
elif a < 0:
    print("Negative")
    print("integer")
else:
    print("Zero")''').font.name = 'Consolas'

doc.add_paragraph()

# 5.2 Greatest Integer (if-elif)
doc.add_heading('5.2 Greatest Integer - Using If-Elif (greatestINT.py)', level=2)
doc.add_paragraph('Finding the greatest of three numbers using conditional statements.')
code = doc.add_paragraph()
code.add_run('''a = int(input("enter a number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a>b and a>c:
    print(a, "is the greatest integer")
elif b>a and b>c:
    print(b, "is the greatest integer")
elif a==b:
    print("First and second numbers are equal and greatest")
elif b==c:      
    print("Second and third numbers are equal and greatest")
elif a==b==c:
    print("All numbers are equal")
else:
    print(c, "is the greatest integer")''').font.name = 'Consolas'

doc.add_paragraph()

# 5.3 Greatest Integer (max)
doc.add_heading('5.3 Greatest Integer - Using max() (greatestinteger.py)', level=2)
doc.add_paragraph('Finding the greatest using the built-in max() function.')
code = doc.add_paragraph()
code.add_run('''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

max_value = max(a, b, c)
print("Greatest integer is: ",max_value)''').font.name = 'Consolas'

doc.add_paragraph()

# 5.4 Grades
doc.add_heading('5.4 Grade Calculator (Grades.py)', level=2)
doc.add_paragraph('Calculating grade based on marks using range.')
code = doc.add_paragraph()
code.add_run('''a = int(input("enter your marks: "))

if a in range(90, 101):
    print("O")
elif a in range (80,90):
    print("A+")
elif a in range (70,80):
    print("A")
elif a in range (60,70):
    print("B+") 
elif a in range (50,60):
    print("B")
elif a in range (40,50):
    print("C")
elif a in range (33,40):
    print("D")  
else:
    print("F")''').font.name = 'Consolas'

doc.add_paragraph()

# 5.5 Grades with Average
doc.add_heading('5.5 Grade Calculator with Average (grades1.py)', level=2)
doc.add_paragraph('Calculating average of 5 subjects and assigning grade.')
code = doc.add_paragraph()
code.add_run('''a = int(input("enter a number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))
e = int(input("enter fifth number: "))

if a > 100 or b > 100 or c > 100 or d > 100 or e > 100:
    print("invalid entry")
elif a < 0 or b < 0 or c < 0 or d < 0 or e < 0:
    print("invalid entry")
else:
    sum = a + b + c + d + e
    avg = sum / 5

    if avg >= 90:
        print("Grade O")
    elif avg >= 80:
        print("Grade A+")
    elif avg >= 70:
        print("Grade A")
    elif avg >= 60:
        print("Grade B+")
    elif avg >= 50:
        print("Grade B")
    elif avg >= 40:
        print("Grade C")
    elif avg >= 30:
        print("Grade D")
    else:
        print("Grade F")''').font.name = 'Consolas'

doc.add_paragraph()

# ============== SECTION 6: LOOPS ==============
doc.add_heading('Section 6: Loops', level=1)

# 6.1 N Numbers
doc.add_heading('6.1 Print N Numbers with Even/Odd Count (n-nUmber.py)', level=2)
doc.add_paragraph('Using for loop to print numbers and count even/odd.')
code = doc.add_paragraph()
code.add_run('''n = int(input("enter a number:"))
odd_count = 0
even_count = 0

for i in range(1,n+1):
    print(i)
    if i%2 == 0:
        even_count = even_count + 1
    else:
        odd_count += 1

print("even numbers= ",even_count)
print("odd numbers= ",odd_count)''').font.name = 'Consolas'

doc.add_paragraph()

# 6.2 Fibonacci
doc.add_heading('6.2 Fibonacci Series (fibonacci.py)', level=2)
doc.add_paragraph('Generating Fibonacci sequence using for loop.')
code = doc.add_paragraph()
code.add_run('''#fibonacci
n = int(input("enter a number: "))

a = 0
b = 1

for i in range (n):
    print(a)
    c = a+b
    a = b
    b = c''').font.name = 'Consolas'

doc.add_paragraph()

# ============== SECTION 7: PROGRAMS ==============
doc.add_heading('Section 7: Practical Programs', level=1)

# 7.1 Swap
doc.add_heading('7.1 Swap Two Numbers (swap.py)', level=2)
doc.add_paragraph('Swapping values using a temporary variable.')
code = doc.add_paragraph()
code.add_run('''a = int(input("enter first number: "))
b = int(input("enter second number: "))

temp  = a
a = b
b = temp

print("after swaping the numbers are: "+str(a)+" "+str(b))''').font.name = 'Consolas'

doc.add_paragraph()

# 7.2 Simple Interest
doc.add_heading('7.2 Simple Interest (simpleintrest.py)', level=2)
doc.add_paragraph('Calculating simple interest: SI = (P × R × T) / 100')
code = doc.add_paragraph()
code.add_run('''p = int(input("enter the principle amount: "))
r = float(input("enter the rate of intrest: "))
t = int(input("enter the time period: "))

si = (p*r*t)/100

print("the simple intrest is: "+str(si)+" frfr")''').font.name = 'Consolas'

doc.add_paragraph()

# 7.3 Compound Interest
doc.add_heading('7.3 Compound Interest (compundintrest.py)', level=2)
doc.add_paragraph('Calculating compound interest: A = P(1 + R/100)^T')
code = doc.add_paragraph()
code.add_run('''P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest (%): "))
T = float(input("Enter the time (in years): "))

A = P * (1 + R / 100) ** T

CI = A - P

print("Final Amount =", A)
print("Compound Interest =", CI)''').font.name = 'Consolas'

doc.add_paragraph()

# 7.4 Celsius to Fahrenheit
doc.add_heading('7.4 Celsius to Fahrenheit (~F-C.py)', level=2)
doc.add_paragraph('Temperature conversion: F = (9/5 × C) + 32')
code = doc.add_paragraph()
code.add_run('''c = int(input("enter the temperature in celsius:"))

f = (9/5*c)+32 

print("the temperature in fahrenheit is: ",f)''').font.name = 'Consolas'

doc.add_paragraph()

# 7.5 Fahrenheit to Celsius
doc.add_heading('7.5 Fahrenheit to Celsius (~C-F.py)', level=2)
doc.add_paragraph('Temperature conversion: C = 5/9 × (F - 32)')
code = doc.add_paragraph()
code.add_run('''f = int(input("enter the temperature in farhenheit: "))
c = (5/9)*(f-32)
print("the temperature in celsius is: "+str(c))''').font.name = 'Consolas'

doc.add_paragraph()

# 7.6 Sum of First and Last Digit
doc.add_heading('7.6 Sum of First and Last Digit (SUMf~l.py)', level=2)
doc.add_paragraph('Finding sum of first and last digit using while loop and string slicing.')
code = doc.add_paragraph()
code.add_run('''n = int(input("enter a number:"))

last = n % 10
first = n 

while first >= 10:
    first //= 10

sum = first + last
print("Sum of first and last digit is:", sum)

#without while loop
first_digit = int(str(n)[0])
last_digit = n % 10
sum_digits = first_digit + last_digit
print("Sum of first and last digit is:", sum_digits)''').font.name = 'Consolas'

doc.add_paragraph()

# 7.7 Number Length
doc.add_heading('7.7 Number Length (numberLen.py)', level=2)
doc.add_paragraph('Finding the number of digits in a number using while loop.')
code = doc.add_paragraph()
code.add_run('''a = int(input("enter a number: "))
c = 0
#using while loop
while(a>0):
  
    c = c + 1
    a//=10
print("length of number is:", c)''').font.name = 'Consolas'

doc.add_paragraph()

# 7.8 Sum of Even Digits
doc.add_heading('7.8 Sum of Even Digits (EvenSUm.py)', level=2)
doc.add_paragraph('Finding sum of all even digits in a number.')
code = doc.add_paragraph()
code.add_run('''n = int(input("enter a number:"))
even_sum = 0

while (n>0):
    digit = n%10
    if digit%2 == 0:
        even_sum = even_sum + digit
    n//=10
print("sum of even digits is:", even_sum)''').font.name = 'Consolas'

doc.add_paragraph()

# ============== SECTION 8: NUMBER PROGRAMS ==============
doc.add_heading('Section 8: Number Theory Programs', level=1)

# 8.1 Armstrong
doc.add_heading('8.1 Armstrong Number (Armstrong.py)', level=2)
doc.add_paragraph('A number is Armstrong if sum of digits raised to power of number of digits equals the number. E.g., 153 = 1³ + 5³ + 3³')
code = doc.add_paragraph()
code.add_run('''# Program to check Armstrong Number

num = int(input("Enter a number: "))
temp = num
sum = 0

# Find number of digits
digits = len(str(num))

# Calculate sum of digits raised to power
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

# Check Armstrong condition
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")''').font.name = 'Consolas'

doc.add_paragraph()

# 8.2 Neon
doc.add_heading('8.2 Neon Number (neon.py)', level=2)
doc.add_paragraph('A number is Neon if sum of digits of its square equals the number. E.g., 9² = 81, 8+1 = 9')
code = doc.add_paragraph()
code.add_run('''a = int(input("enter a number:"))
n = a**2
sum = 0

while n>0:
    digit = n%10
    sum  = digit + sum
    n//=10

if sum == a:
    print(a, "is a neon number")
else:
    print(a, "is not a neon number")''').font.name = 'Consolas'

doc.add_paragraph()

# 8.3 Harshad Number
doc.add_heading('8.3 Harshad Number (harshadnumber.py)', level=2)
doc.add_paragraph('A number is Harshad (Niven) if it is divisible by the sum of its digits. E.g., 18 → 1+8=9, 18÷9=2')
code = doc.add_paragraph()
code.add_run('''n = int(input("Enter a number: "))

sum = 0
temp = n

while n > 0:
    digit = n % 10
    sum = sum + digit
    n //= 10

if temp % sum == 0:
    print("It is a Harshad number")
else:
    print("It is not a Harshad number")''').font.name = 'Consolas'

doc.add_paragraph()

# 8.4 Palindrome (Method 1)
doc.add_heading('8.4 Palindrome - Using While Loop (pallendrome.py)', level=2)
doc.add_paragraph('A number that reads the same forward and backward. Using digit extraction method.')
code = doc.add_paragraph()
code.add_run('''a = int(input("enter a number: "))
rev = 0
temp = a
while temp>0:
    digit = temp%10
    rev = rev*10 + digit
    temp//=10
if rev == a:
    print(a,"is a pallendrome number")
else:
    print(a,"is not a pallendrome number")''').font.name = 'Consolas'

doc.add_paragraph()

# 8.5 Palindrome (Method 2)
doc.add_heading('8.5 Palindrome - Using String Slicing (pallendrome(1).py)', level=2)
doc.add_paragraph('Checking palindrome using Python string slicing [::-1].')
code = doc.add_paragraph()
code.add_run('''a = str(input("enter a number: "))
temp = a[::-1]
if temp == a:
    print(a,"is a pallendrome number")
else:
    print(a,"is not a pallendrome number")''').font.name = 'Consolas'

# Save the document
doc.save('C:/Users/saima/OneDrive/Documents/Sem 2/learning python/Python_Code_Collection.docx')
print("Document created successfully: Python_Code_Collection.docx")
