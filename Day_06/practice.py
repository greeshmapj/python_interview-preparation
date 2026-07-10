# 1. Print every character of a string using a loop.
word = input('Enter a word: ')
for char in word:
    print(char)

# 2. Print a string in reverse.
word = input('enter a word: ').lower()
rev_word = ""
for i in range(len(word)-1,-1,-1):
    rev_word += word[i]
print(rev_word)

# 3. Count vowels.
word = input('enter a word: ').lower()
vowels = 'a','e','i','o','u'
count = 0
for char in word:
    if char in vowels:
        count+=1
print(count)

# 4. Count consonants.
word = input('enter a word: ').lower()
vowels = 'a','e','i','o','u'
count = 0
for char in word:
    if char not in vowels and char.isalpha():
        count+=1
print(count)

# 5. Check whether two strings are anagrams.
word1 = 'listen'
word2 = 'silent'
print(sorted(word1)==sorted(word2))

# 6.find the first non-repeating character.
word = 'aabbccdbe'
freq = {}
for i in word:
    freq[i] = freq.get(i,0)+1
for i in word:
    if freq[i]==1:
        print(i)
        break
        
# 7. Remove all spaces from a sentence.
sentence = 'Hello AI Engineer'
print(sentence.replace(" ",""))

# 8. Count the occurrence of each word.
word = 'this is is python python python'
word_list = word.split()     #['this', 'is', 'is', 'python', 'python', 'python']
freq = {}
for char in word_list:
    freq[char] = freq.get(char,0)+ 1
print(freq)

# 9. Find the longest word in a sentence.(not right)
sentence = 'I love artificial intelligence'
list_word = sentence.split()
longest = list_word[0]
for i in list_word:
    if len(i) > len(longest):
        longest = i
print(longest)

#10. Check whether a string contains only digits.
number1 = '123456'
word = '12a45'
print(number1.isdigit())
print(word.isdigit())

#DEBUGGING

# Debug 1.
word = "Python"
# word[0] = "J"  # string is immutable so we cannot chane the characters in the string after creation we can only create a new variable and update it.
word = word.replace("P","J")
print(word)

#Debug 2.
name = "Greeshma"
print(name.upper())


#Debug 3.
sentence = "Python AI"
words = sentence.split()







