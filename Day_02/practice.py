# 1.Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

# 2.Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)

# 3. Print all even numbers from 1 to 50.
for i in range(1,51):
    if i%2==0:
        print(i)

# 4. Print all odd numbers from 1 to 50.
for i in range(1,51):
    if i%2!=0:
        print(i)

# 5.Print the multiplication table of any number.
num = int(input("enter a number: "))
for i in range(1,11):
    print(num , '*', i ,'=', num*i)

# 6. Find the sum of numbers from 1 to 100.
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)


#7.Find the factorial of a number using a loop.
num = int(input("enter a number: "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)

# 8. Reverse a string using a loop.
word = input("enter a word: ").lower()
reverse = ""
for i in range(len(word)-1,-1,-1):
    reverse += word[i]
print(reverse)

# 9. Check whether a string is a palindrome.(wrong)
#the logic is to reverse the string and to see if the string in both conditions are equal.
word = input("enter a word: ").lower()
reverse = ""
for i in range(len(word)-1,-1,-1):
    reverse += word[i]
if reverse==word:
    print("its a palindrome")
else:
    print("not a palindrome")

# 10. Count vowels in a string.
vowel = ['a','e','i','o','u']
str = input('enter a word: ')
count = 0
for i in str:
    if i in vowel:
        count +=1
print(count)



