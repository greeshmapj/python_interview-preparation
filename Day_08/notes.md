1. What is an Exception?
Definition - An exception is an unexpected runtime error that interrupts the normal flow of a program. If it is not handled, it may terminate the program. 
Why exceptions occur - Exception occurs when the syntactically correct code encounters a runtime error that can can crash the program flow.
Difference between Syntax Error and Exception - 
Syntax error - Occurs when the programmer makes a gramatical error in the code.
eg: if x>5 , print(Hello), for i in range[], etc


2. Why do we use Exception Handling?
We use exception handling to manage any unexpected error that can affect the flow of the program
Give at least 3 real-world examples.
1. Trying to open a file that doesn't exist.
2. User enters text instead of a number.
3. ATM transaction fails due to insufficient balance.
4. Network connection lost while downloading data.

3. Explain
try - the part where we write the code which has the possible exception
except - except catches and handles the exception so the program can continue executing gracefully.
else - executes if the exception doesn't occur
finally - executes irrespective of whether an exceptin is present or not.
Give one example for each.
numerator = 5
denominator = 1
try:
    result = numerator/denominator
except ZeroDivisionError as zde:
    print("Division by zero is not possible",zde)
else:
    print("result",result)
finally:
    print("End of program")  

4. Common Exceptions
Explain with one example each.
ZeroDivisionError
ValueError
eg:
try:
    numerator = int(input("Enter a number 1: "))
    denominator = int(input("Enter a number 2: "))
    result = numerator/denominator
except ZeroDivisionError as zde:
    print("Division by zero is not possible",zde)
except ValueError as ve:
    print("use a numeriacl digit please",ve)
else:
    print("result",result)
finally:
    print("End of program")

TypeError
try:
    age = 22
    print(5+'3')
except TypeError as typ:
    print("incorrect usage of operator, please recheck",typ)

NameError
try:
    name = 'Alice'
    print(Name)
except NameError as ne:
    print(ne)

IndexError
try:
    fruits = ['apple','banana','grapes']
    fruits[6]
except IndexError as ie:
    print(ie)

KeyError
try: 
    user = {"name": "Greeshma", "age": 22}
    print(user["email"])
except KeyError as ke:
    print(ke)

FileNotFoundError
try: 
    file = open("Day_07/sample.txt","r")
    print(file.read())
except FileNotFoundError as fe:
    print("Please cross-check the location of the file",fe)


5. What is raise? Why do we use it?
raise is used to deliberately create an exception when a program detects an invalid condition.
eg:
age = -12
if age < 0:
    raise ValueError("age cannot be negative")

6. difference between except Exception vs specific exception
except exception catches most runtime exceptions while the specific targets only the defined one.

raise vs print
raise is used to intentionally stop the program flow under unfavourable circumstances
print displays an output in the console for the user to see.
