# DICTIONARY
# 1. Create the following dictionary and print values
details = {
    'Name': 'Greeshma',
    'Age' : 22,
    'City' : 'Kochi'
}
print(details.values())  

# 2.Update the city.
details.update({'City':'kottayam'})

#3. Add a new key
details['Profession'] = 'AI Engineer'

# 4. delete age
details.pop('Age')

# 5. Print all keys.
print(details.keys())

#6. Print all values.
print(details.values())

#7. Loop through a dictionary.
for key, value in details.items():
    print(key, ":", value)


#8. Count the frequency of each character.
word = "banana"
freq = {}
for char in word:
    freq[char] = freq.get(char,0) + 1
print(freq)    # -- output - {'b': 1, 'a': 3, 'n': 2}

#9. Find the most frequent character.
largest = 0
character = ""
for key,value in freq.items():
    if value > largest:
        largest=value
        character = key
print(character)

#10. Merge two dictionaries.
student = {
    "name":"Greeshma"
}
marks = {
    "python":95
}
merged_dict = student | marks
print(merged_dict)

#SETS
# 1. create {1,2,3,4}
numbers = set()
for i in range(1,5):
    numbers.add(i)

#2. add 5
numbers.add(5)

#3. remove 3
numbers.remove(3)

#4. create 2 sets and find union,intersection and difference
A = {1,2,3}
B = {3,4,5}
print(A.union(B))   #--output - {1, 2, 3, 4, 5}
print(A.intersection(B))  #--output - {3}
print(A.difference(B))    #--output -  {1,2}

#5. Remove duplicates 
numbers = [1,2,2,3,4,4,5]
new_numbers = set(numbers)
print(new_numbers)    

 #################################################################

 #DEBUGGING

 # Debug 1.
"""
student = {
"name":"Greeshma",
"age":24
}

print(student(name))
"""

print(student['name'])

# Debug 2.
"""
A = {1,2,3}
A.append(4)
"""

A.add(4)

# debug 3.
"""
student = {}
student["name"] = "Greeshma"
student["age"] += 24
"""
student["age"] = 24





