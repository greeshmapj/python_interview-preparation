STRINGS

1. What is a String?
Immutable sequence of characters enclosed within single, double or triple quotes used to represent textual data in python
syntax - ' '/" "/''' '''

2. Characteristics of Strings
Explain each with examples.
Immutable - Attempts to alter a character results in error, we can only create a new string with changes using different functions.
eg : 
message = 'Hello World'
message = message.replace('World','Universe')
print(message)    # Hello World

To make the changes to the variable:
message = message.replace('World','Universe')  #create a new variable
print(message)

Ordered - characters in string has a fixed location, they cannot change their location
eg : word = 'banana'
    print(word)  #'banana' -- prints in the exact order

Supports indexing - Since strings are ordered it supports indexing
eg: word = 'banana'
    print(word[2])  #'n'

Supports slicing - we can fetch a sequence of characters from the string using its positive or negative index.
eg: 
sentence = "Ilovepython"
print(sentence[3:])  # 'vepython'
print(sentence[-5:-2])   # 'yth'

Allows duplicates - duplicate characters are allowed
eg: word = 'banana'   #there are multiple 'a' and 'n' in this string

Can store special characters - Strings are immutable sequence of unicode characaters
eg : message = "He!!o my number is 89#*%>/_** and i have lot's of $$$"

3. String Indexing
Explain
Positive indexing - the use of positive numbers
Negative indexing - the use of negative numbers
eg: 
word = "Ilovepython"
print(word[3])  # 'v'
print(word[-5])   # 'y'

4. String Slicing
eg:
word = "Ilovepython"
this string has got indexing 0 to 10 from left end and -1 to -11 starting from right end.
word[2:5] - 'ove' 
word[:4] - 'Ilov' (starts from 0)
word[3:] -  'vepython' (ends with tle last character of the string)
word[::2] - 'Ioeyhn' (does slicing with break of 2)
word[::-1] - 'nohtypevolI' (reverse the string)

5. Common String Methods
lower() - converts the string to lowercase
print('Hello'.lower())  - hello

upper() - converts the string to uppercase
print('Hello'.upper()) - HELLO
 
title() -  each word starts with a capital letter
print('hello world'.title()) - Hello World

capitalize() - makes the first letter of the first word in the sequence capital
print('hello world'.capitalize()) - Hello world          

strip() - Return a copy of the string with leading and trailing whitespace removed.
print(' hello world '.strip()) - hello world

replace() - creates a copy of the string with changes applied
message = 'Hello World'
message.replace('World','Universe')
print(message)    # Hello World

split() - return a list of the substrings in the string, using sep as the separator string.
print('hello world'.split())   - ['hello', 'world']

join() - helps merge the items of an iterable to a single string using a spectfic delimitter
greet = ['hi',' hello',' hw are you']
print(",".join(greet))

find() - returns the index of the substring passed
word = 'banana in tree'
print(word.find('in')) - 7

count() - returns the number of occurence of the substring
word = 'banana in tree'
print(word.count('an'))  - 2

startswith() - returns true if the string starts with the intended prefix
word = 'banana in tree'
print(word.startswith('b'))  - True

endswith() - returns true if the string ends with the intended suffix
word = 'banana in tree'
print(word.endswith('pe'))   - False

isalpha() - returns true if the string contains only alphabetic characters
word = 'banana in tree'
print(word.isalpha())   - False

isdigit() - returns true if the characters are entirely digits only
word = '1234'
print(word.isdigit())  - True

isalnum() - returns true if the characters of the string are mix of alphabets and numeric digits(alpha-numeric)
word = '1234abc'
print(word.isalnum()) - True

6. String Operators
+ - possible for concatnating two strings
greet = 'Hello'
name = 'Greeshma'
print(greet + name)

* - helps multiply an integer with a string allowing replication
print('Hi'+'bye'*2)  - Hibyebye

in - checks if it exists
print('h' in 'hello') - True
print('m' in 'hello') - False

not in - checks if it doesn't exist
print('h' not in 'hello') - False 

7. Difference
replace() vs strip() - 
replace substitutes the text anywhere in the string
fruits = "orange apple banana"
print(fruits.replace("apple","pineapple")) - "orange pineapple banana"
Strip only removes characters from the outer edges  of the string.
fruits = "??orange apple banana?"
print(fruits.strip("?")) - "orange pineapple banana"

find() vs index() - if we search for a non-existent substring we get an error where as find gives -1 as the output if wrong values are passed

split() vs join() - return a list of the substrings in the string, using sep as the separator join but helps merge the items of an iterable to a single string using a spectfic delimitter

lower() vs casefold() - lower() converts ASCII uppercase characters to lowercase where as casefold() is used for caseless matching across multilingial unicode text.

isalpha() vs isalnum() - isalpha() can have only alphabetic characters but isalnum() can have both alphabets and numericals.

8. Escape Characters
\n - new line
sentence = 'I \n love python'  - output - I 
                                        love python

\t - means tab
sentence = 'I \t love python'  - output - I     love python 

\\ - means backslash
path = "C:\\Users\\Greeshma"
print(path)  -- output - C:\Users\Greeshma

\' - displays the single quote after the back slash
sentence = 'it\'s a rainy day'
print(sentence)   - output - it's a rainy day

\" - displays the single quote after the back slash
sentence = 'it\"s a rainy day'
print(sentence)   - output - it"s a rainy day

9. why are f-strings prepared?
these helps us avoid long, clumsy, confusing concatenation thus allowing concise, readable way of embedding variables and expression in string literals.
name = "Greeshma"
print(f"My name is {name}") - output - My name is Greeshma
f represent formatted string 

10. Real-world Uses of Strings
 1. data documentation
 2. spell checkers
 3. Email validation
 4. Log files
 5. AI prompts



Interview nuggets

Largest number → compare values.
Longest word → compare len() of words.
First non-repeating character → use a frequency dictionary, then scan the original string.
Anagram → compare the sorted versions of both strings.