#FUNCTIONS

# 1.create a fn to print 'Hello AI Engineer'
def greet():
    print('Hello AI Engineer')
greet()

# 2.Create a function that takes a name and prints
def greet(name):
    print("Hello",name)
    
name = input('enter a name: ')
greet(name)

# 3. Create a function that adds two numbers.
def add(num1,num2):
    print(num1, '+', num2,'=',num1+num2)
    
num1 = int(input('enter a number,num1: '))
num2 = int(input('enter a number,num2: '))
add(num1,num2)

# 4. Create a function that returns the square of a number.
def square(num):
    return num*num

num = int(input("Enter a number: "))
square(num)

# 5. Create a function that checks whether a number is even or odd.
def OddEven(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

num = int(input("Enter a number: "))
OddEven(num)

# 6. Create a function that returns the largest of three numbers.
def Largest(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(num1,'is largest')
        else:
            print (num3,'is largest')
    else:
        if num2>num3:
            print(num2,'is largest')
        else:
            print (num3,'is largest')
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
Largest(num1,num2,num3)

# 7. Create a function to count vowels in a string.
def vow(word):
    vowel = ['a','e','i','o','u']
    count = 0

    for i in word:
        if i in vowel:
            count +=1
    print(count)

word = input('enter a word: ').lower()
vow(word)

# 8. Create a function that reverses a string.
def Reverse(word):
    rev = ""
    for i in range(len(word)-1,-1,-1):
        rev += word[i]
    return rev

word = input("Enter a word: ").lower()
Reverse(word)

# 9. Create a function that checks whether a word is a palindrome.
def Reverse(word):
    rev = ""
    for i in range(len(word)-1,-1,-1):
        rev += word[i]
    return rev

def is_palindrome(word,rev):
    if rev == word:
        print("its a palindrome")
    else:
        print("not a palindrome")

word = input("Enter a word: ").lower()
rev = Reverse(word)    
is_palindrome(word,rev)

#not correct, this is what i could do.

#10. Create a simple calculator. (not fully correct)
def Calculator(num1,num2,option):
    add = num1 + num2
    subtract = num1 - num2
    multiply = num1*num2
    divide = num1/num2
    if option == 'add':
        print('sum is',add)
    elif option == 'subtract':
        print('difference is',subtract)
    elif option == 'multiply':
        print('Product is',multiply)
    elif option == 'divide':
        print('fraction is',num1/num2)
    else:
        print("invalid option")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
option = input("Enter which operation you want(add,subtract,multiply,divide): ")
Calculator(num1,num2,option)
