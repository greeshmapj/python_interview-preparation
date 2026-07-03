#1. print 'hello AI Engineer'
print('Hello AI Engineer')

#2.Store your name, age and city in variables and print them.
name = 'Greeshma'
age = 22
city = 'Kochi'
print(name,age,city)

#3. Swap two numbers.
x = int(input("enter a number,x : "))
y = int(input("enter a number,y : "))

#method 1
temp = x
x = y 
y = temp

#method 2
# x,y = y,x

print(x)
print(y)

#4. Find the largest of three numbers.
x = int(input("enter a number x: "))
y = int(input("enter a number y: "))
z = int(input("enter a number z: "))
if x>y:
    if x>z:
        print('x is largest')
    else:
        print ('z is largest')

else:
    if y>z:
        print('y is largest')
    else:
        print ('z is largest')

#5.Check whether a number is even or odd. 
num = int(input("enter a number : "))
if num%2==0:
    print("number is even")
else:
    print("number is odd")


#6. Check whether a year is a leap year.
year = int(input("enter an year of choice : "))
if year%4==0 and year%100!=0:
    print('its a leap year')
else:
    print('not a leap year')

#7.Find the factorial of a number.
num = int(input("enter a number : "))
#5! = 5*4*3*2*1
#factorial of n = n(n-1)!



#8. Reverse a string.
# x = input('enter a word: ')

#9. Check whether a string is a palindrome.





