#1. Handle division by zero without crashing
try:
    num1 = 10
    num2 = 0
    result = num1/num2
except ZeroDivisionError as zde:
    print("Cannot divide by zero.")


#2. Take user input. If the user enters a non-number,
try:
    num = int(input("Enter a number : "))
    print(num)
except ValueError:
    print('Please enter a valid integer.') 

#3. Access an invalid list index safely.
try:
    numbers = [10,20,30]
    numbers[6]
except IndexError as ie:
    print(ie) 

#4. Access a missing dictionary key safely.
try: 
    user = {"name": "Greeshma", "age": 22}
    print(user["email"])
except KeyError as ke:
    print(ke)

#5. Open a file safely. If the file doesn't exist, print 'File Noyt Found'
try: 
    with open("Day_07/sample.txt","r")as file:
        print(file.read())
except FileNotFoundError as fe:
    print("File not found",fe) 

#6. Calculator
# Handle division by zero & invalid operation using exceptions.
try:
    num1 = int(input("Enter a number 1: "))
    num2 = int(input("Enter a number 2: "))
    operator = input("Enter an operator(+,-,*,/): ")
    if operator == "+":
        print('The sum is ',num1 + num2)
    elif operator == "-":
        print('the difference is ',num1 - num2)
    elif operator == "*":
        print('the product is ',num1 * num2)
    elif operator == "/":
        print('the fraction is ',num1 / num2)
    else:
        raise ValueError("Invalid Opration")
    
except ZeroDivisionError as zde:
    print("Division by zero is not possible",zde)
except ValueError as ve:
    print("Error",ve)
finally:
    print("End of program")


#7. Create your own exception.If age < 18 raise ValueError
try:    
    age = int(input("enter your age: "))
    if age < 18:
        raise ValueError("age must be atleast 18")
except ValueError as ve:
    print("access denied",ve)

#8. Ask the user for a positive number. If negative, raise an exception.
try:    
    num = int(input("enter a positive number: "))
    if num < 0:
        raise ValueError("number must be positive")
except ValueError as ve:
    print("Invalid input",ve)
else:
    print("the number is",num)

#9. Use try, except, else,finally all together
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

#10. create a function safe_divide(a,b) return division result if valid, else invalid division.
def safe_divide(a,b):
    try:
        return a/b
    except (ZeroDivisionError,TypeError)as e:
        return 'Invalid division'
    
print(safe_divide(10,0))






 


