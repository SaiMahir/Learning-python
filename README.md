# Learning Python

A repository for learning Python fundamentals and best practices.

---

## 📚 Programs in Order of Learning

### 1. Basics - Getting Started
| # | File | Topic |
|---|------|-------|
| 1 | [syntax.py](syntax.py) | First program - print() statements |
| 2 | [keywords.py](keywords.py) | Python reserved keywords |

### 2. Variables & Data Types
| # | File | Topic |
|---|------|-------|
| 3 | [variableint.py](variableint.py) | Integer variables |
| 4 | [variablefloat.py](variablefloat.py) | Float variables |
| 5 | [variablestring.py](variablestring.py) | String variables |
| 6 | [variableboolean.py](variableboolean.py) | Boolean variables |
| 7 | [multipleAssignment.py](multipleAssignment.py) | Assigning multiple variables |

### 3. Input/Output & Type Casting
| # | File | Topic |
|---|------|-------|
| 8 | [input.py](input.py) | Taking user input |
| 9 | [inputADD.py](inputADD.py) | Adding two input numbers |
| 10 | [typecasting.py](typecasting.py) | Converting data types |
| 11 | [format.py](format.py) | Escape characters (\n, \t) |

### 4. Operators
| # | File | Topic |
|---|------|-------|
| 12 | [operators.py](operators.py) | All operators (arithmetic, relational, logical, bitwise) |
| 13 | [operators[extra].py](operators[extra].py) | Additional operator examples |

### 5. Strings
| # | File | Topic |
|---|------|-------|
| 14 | [stringbasics.py](stringbasics.py) | String methods (len, find, upper, lower, etc.) |
| 15 | [indexing.py](indexing.py) | String indexing and reversing |
| 16 | [Slicing.py](Slicing.py) | String slicing |

### 6. Conditional Statements
| # | File | Topic |
|---|------|-------|
| 17 | [Check_no.py](Check_no.py) | If-else conditions |
| 18 | [positiveNegitive.py](positiveNegitive.py) | Check positive/negative |
| 19 | [evenoddFunc.py](evenoddFunc.py) | Check even or odd |
| 20 | [Grades.py](Grades.py) | Grade calculator (if-elif-else) |
| 21 | [grades1.py](grades1.py) | Another grade example |
| 22 | [Identify.py](Identify.py) | Identify number properties |
| 23 | [greatestINT.py](greatestINT.py) | Find greatest of numbers |
| 24 | [greatestinteger.py](greatestinteger.py) | Greatest integer function |

### 7. Loops
| # | File | Topic |
|---|------|-------|
| 25 | [n-nUmber.py](n-nUmber.py) | Loop through n numbers |
| 26 | [EvenSUm.py](EvenSUm.py) | Sum of even numbers |
| 27 | [SUMf~l.py](SUMf~l.py) | Sum from first to last |
| 28 | [numberLen.py](numberLen.py) | Find length of number |

### 8. Math Programs
| # | File | Topic |
|---|------|-------|
| 29 | [mathfunc.py](mathfunc.py) | Math functions |
| 30 | [calc.py](calc.py) | Calculator program |
| 31 | [simpleintrest.py](simpleintrest.py) | Simple interest |
| 32 | [compundintrest.py](compundintrest.py) | Compound interest |
| 33 | [~C-F.py](~C-F.py) | Celsius to Fahrenheit |
| 34 | [~F-C.py](~F-C.py) | Fahrenheit to Celsius |
| 35 | [swap.py](swap.py) | Swap two numbers |

### 9. Number Theory Programs
| # | File | Topic |
|---|------|-------|
| 36 | [fibonacci.py](fibonacci.py) | Fibonacci series |
| 37 | [pallendrome.py](pallendrome.py) | Palindrome check |
| 38 | [pallendrome(1).py](pallendrome(1).py) | Another palindrome method |
| 39 | [Armstrong.py](Armstrong.py) | Armstrong number |
| 40 | [neon.py](neon.py) | Neon number |
| 41 | [harshadnumber.py](harshadnumber.py) | Harshad number |

### 10. Lists
| # | File | Topic |
|---|------|-------|
| 42 | [arthemeticList.py](arthemeticList.py) | List basics |
| 43 | [listFunc.py](listFunc.py) | List methods (len, max, min, sort, etc.) |
| 44 | [repetedElement.py](repetedElement.py) | Find repeated elements |

### 11. Functions
| # | File | Topic |
|---|------|-------|
| 45 | [addFunc.py](addFunc.py) | Basic function definition |
| 46 | [funcNnum.py](funcNnum.py) | Functions with numbers |

### 12. Problem Solving
| # | File | Topic |
|---|------|-------|
| 47 | [prob.py](prob.py) | Practice problem 1 |
| 48 | [prob1.py](prob1.py) | Practice problem 2 |
| 49 | [prop2.py](prop2.py) | Practice problem 3 |
| 50 | [prob4.py](prob4.py) | Count occurrences & negatives in list |
| 51 | [prob4(1).py](prob4(1).py) | Count element occurrences |
| 52 | [listP3.py](listP3.py) | List problem - count with validation |

### 13. Libraries & Advanced
| # | File | Topic |
|---|------|-------|
| 53 | [libraries.py](libraries.py) | Using Python libraries |
| 54 | [create_doc.py](create_doc.py) | Creating documents with python-docx |

---

## 🛠️ Setting Up a Virtual Environment

You must create a virtual environment for your Python code to run in.

### Why Use Virtual Environments?

If you don't create a virtual environment, all Python packages will be installed globally. This means they are not separated or isolated between projects.

This won't be a problem for basic code since we won't be installing any libraries or different versions of the same libraries. However, if we need to install libraries in the future, they may conflict. For example:
- One project needs **Django 3.0**
- Another project needs **Django 4.0**

If both are running globally, installing one version will break the other project.

### Commands

**Create a virtual environment:**
```powershell
python -m venv EnvironmentName
```

**Activate the environment (Windows PowerShell):**
```powershell
.\EnvironmentName\Scripts\Activate.ps1
```

**Activate the environment (Command Prompt):**
```cmd
.\EnvironmentName\Scripts\activate.bat
```

**Deactivate the environment:**
```powershell
deactivate
```

> **Note:** If you get an execution policy error when activating, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```