1. What is a Dictionary?
A dictionary is a mutable mapping that stores data as key-value pairs, represented using dict() or {}.
eg: {
    'name':'Greeshma,
    'age':22,
    'place':'Kochi'
}

2. Why do we use Dictionaries?
we use dictionaries when we want to store the data in key value format and dictionaries provide fast lookup using keys.

3. Dictionary Syntax - dict() or {key:Value}

4. Characteristics of Dictionaries
Mutable - The dictionary itself is mutable.
Keys must be immutable types (like int, str, tuple).Values can be mutable or immutable
eg: student = {
    "marks": [90, 95]
}

Key-Value pairs - each data stored in key-value format, one key can have only 1 value, if more than 1 value is given then the last provided will be chosen
eg :
dict = {1:'hi',2:'hello',3:'mm',2:'hurray'}
print(dict)  -- output - {1: 'hi', 2: 'hurray', 3: 'mm'}

Unique keys - keys are immutable and need to be unique, no duplicates allowed

Values can be duplicated - values can be duplicated, i.e 2 keys can have the same value
eg: dict = {1:'hi',2:'hello',3:'hi'}
    print(dict)

Ordered (Python 3.7+) - dictionary is an ordered collection from python 3.7+ version i.e we can fetch a value using its key but before this version dictionary was an unordered collection.

5. What is a Set? - Set is an unordered, heterogenous collection of variables represented using set() that stores unique elements.
eg : set = {1,2.2,'greeshma',False}
     print(set)   -- output - {False, 1, 2.2, 'greeshma'}

6. Difference between List, Tuple, Dictionary and Set
list       - Mutable,                      Duplicates allowed,    ordered,  [],    heterogenous
Tuple      - Immutable,                    Duplicates allowed,    ordered,  (),    heterogenous
Set        - Mutable,                      No duplicates allowed,unordered, set(), heterogenous
Dictionary - (key-immutable,value-mutable),duplicates allowed,  ordered, {},    heterogenous

7. Common Dictionary Methods
get() - used to fetch a value using its key.
eg : dict = {1:'hi',2:'hello',3:'hi'}
    print(dict.get(1))  --output - hi

keys() - used to fetch all keys in the dictionary
eg :dict = {1:'hi',2:'hello',3:'hi'}
    print(dict.keys())  --output - dict_keys([1, 2, 3])

values() - used to fetch all values in the dictionary
eg :dict = {1:'hi',2:'hello',3:'hi'}
    print(dict.values())  --output - dict_values(['hi', 'hello', 'hi'])

items() - used to fetch all the key-value pairs of the dictionary
eg :dict = {1:'hi',2:'hello',3:'hi'}
    print(dict.items())  --output - dict_items([(1, 'hi'), (2, 'hello'), (3, 'hi')])

update() - used to update the items of dictionary
eg :
dict = {1:'hi',2:'hello',3:'hi'}
dict.update({3:'mummy'})
print(dict)

pop() - used to remove a  specific value by passing its key and return it. if no key passed or wrong key passed throws a 'keyerror'
eg :
dict = {1:'hi',2:'hello',3:'hi'}
print(dict)       -- output - {1: 'hi', 2: 'hello', 3: 'hi'}
print(dict.pop(2)) -- output - hello

popitem() - used to remove the last key-value pair and return it.
eg :
dict = {1:'hi',2:'hello',3:'hi'}
print(dict)     -- output - {1: 'hi', 2: 'hello', 3: 'hi'}
print(dict.popitem())  --output - (3, 'hi')

clear() - used to clear all the data from the dictionary
eg :dict = {1:'hi',2:'hello',3:'hi'}
dict.clear()
print(dict) -- output - {}

8. Common Set Methods
add() - used to add a variable to the set
eg :
set = {10,20,30,40}
set.add(50)
print(set)  -- output - {40, 10, 50, 20, 30}

remove() used to remove a variable from the set
eg: 
set = {10,20,30,40}
set.remove(20)
print(set)  -- output - {40, 10, 30}

discard() - used to remove an item but unlike remove it does not throw an error if a wrong key is passed instead given the entire set as output
eg:
set = {10,20,30,40}
set.discard(60)
print(set)  --output - {40, 10, 20, 30}

union() - used to get all the variables from all intended sets
eg:
set1 = {10,20,30,40}
set2 = {100,200,309}
set = set1.union(set2)
print(set)   --output - {20, 100, 309, 40, 10, 30, 200}

intersection() - used to fetch the common variable from the set1 that matches with set2
eg : 
set1 = {10,20,30,40,100}
set2 = {100,200,309}
set = set1.intersection(set2)
print(set)  --output - {100}

difference() - used to fetch all the variables from the set1 that is not present in set2
eg:
set1 = {10,20,309,4100}
set2 = {100,200,309}
set = set1.difference(set2)
print(set) -- output - {10,20,4100}

clear() - used to remove the entire items from the set
eg:
set = {10,20,30,40}
set.clear()
print(set)   -- output - set()

9. Difference
remove() vs discard()
remove throws an error in case of a wrong key being passed but discard does not throw an error instead given the entire set as output

get() vs [] - if a wrong key is passed to [] it throws an error and 'get'  gives 'None' as the output and does not throw an error.

pop() vs popitem() - pop is used to remove a  specific value by passing its key and return it, if no key passed or wrong key passed throws a 'keyerror'. popitem is used to remove the last key-value pair and to return it.

update() vs add() - update is used for updating a dictionary where as add function is used for sets

10. Real-world examples, Give at least three examples each.
Where are dictionaries used?
1. for storing students data
eg : roll_no = {
    1:'Jaames',
    2:'Mary'
}
2. for storing students marks
eg : remya : {
    'maths' : 68,
    'physics' : 77,
    'biology' : 80
}
3. grocery shopping list
grocery(kg) = {
    'rice' : 1,
    'sugar' : 0.5,
    'millets' : 2
}

Where are sets used?
1. for storing  email details
emails = {
"a@gmail.com",
"b@gmail.com"
}
 2. class subjects details
 subjects = {'maths','biology','physics','english'}
 3. phone number data collection
 phone = {1111,234,222,565}

 Difference between dictionary and JSON.
 The core difference is that a dictionary is an in-memory data structure used to manipulate data within a specific programming language (like Python), whereas JSON is a text-based data format used to transfer and store data across different systems

