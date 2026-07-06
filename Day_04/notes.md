LISTS

1. What is a List?
A list is an ordered, mutable collection in Python that can store multiple values, including values of different data types. Lists are represented using square brackets [].
eg: numbers = [1,2,5,7,90]

2. Why do we use Lists?
- we need subsequent modification of the values 
- store multiple values
- dynamically add/remove items
- iterate over collections
fruits = ["apple", "banana", "orange"]
fruits.append("grapes")
print(fruits)

3. List Syntax 
my_lst = [1,2,3]

4. Characteristics of Lists
Ordered - list has got indexing meaning objects have got a fixed position 
eg: fruits = ["apple", "banana", "orange"]
    print(fruits[1])  -- banana

Mutable - the elements can be varied later after its creation
eg :    fruits = ["apple", "banana", "orange"]
        fruits.remove('banana')
        print(fruits)

Allows duplicates - list allows duplicate values
eg : num = [2,5,7,11,80,55,7,11]

Can store different data types - we can create a with different data types
eg: num = ['mary',23,'kochi']

5. What is a Tuple?
A tuple is an ordered, immutable collection represented using parentheses ().

6. Difference between List and Tuple
List - Mutable, represented using [], slower, more memory, can perform more operations on elements, Lists are generally used when data changes. 
Tuple - Immutable, represented using (), faster, less memory, limited operations possible, Tuples are used when data should remain constant.

7. List Indexing
list is ordered hence has got index which can be used to fetch a particular element from the list
Positive indexing - if we are starting from the left end we got index as positive numbers like 0,1,2,3,..(len-1)
eg: fruits = ["apple", "banana", "orange"]
    fruits[1] - 'banana'
Negative indexing - we got negative numbers if we are starting from right end like -1,-2,-3,...
eg: fruits[-2] - banana

8. List Slicing - the process of fetching a portion of list is called slicing
fruits = ["apple", "banana", "orange","grapes","mango","pineapple"]
print(fruits[2:]) - ["orange,"grapes","mango","pineapple"]

9. Common List Methods
fruits = ["apple", "banana", "orange"]
append() - used to add an object to the list towards its end as a single object
eg :  fruits.append(['go','bu']) --- output - ['apple','banana','orange',['go','bu']]

extend() - similar to append but used to extend the list one by one
eg:  fruits.extend(['go','bu']) --- output - ['apple','banana','orange','go','bu']

insert() - used to add and object to a particular location based on index
eg : fruits.insert(1,'bu')   -- output - ['apple', 'bu', 'banana', 'orange']

remove() - used to remove the first occurence of the object.If no objects passed it throws an error
eg : fruits.remove('banana') -- output - ['apple', 'orange']

pop() - used to remove the last object by default. and if index passed removes the element at that index.
eg : fruits.pop() -- output - ['apple', 'banana']

clear() - used to clear all objects in the list
eg : fruits.clear() -- output - []

sort() - used to sort the objects in ascending order by default
eg :    fruits = ["apple", "banana", "orange",'grapes','almond']
        fruits.sort()  --output - ['almond', 'apple', 'banana', 'grapes', 'orange']
        
reverse() - reverses the current order, no sorting involved.
eg :    fruits = ["apple", "banana", "orange",'grapes','almond']
        fruits.reverse() --output - ['almond', 'grapes', 'orange', 'banana', 'apple']

count() - gives us the number of times an object is present
eg :    fruits = ["apple", "banana", "orange",'grapes','apple']
        print(fruits.count('apple'))  -- output - 2

index() - a method that returns the position of an element.
eg : index of banana is 1

10. Built-in Functions on Lists
len() - gives the length of list
eg :    fruits = ["apple", "banana", "orange",'grapes','apple']
        print(len(fruits))

sum() - gives the sum of intended objects, by default gives the sum of all objects, applicable to list containing numerical objects
eg :    num = [1,2,11,5]
        print(sum(num))

max() - gives the largest object
eg: fruits = ["apple", "banana", "orange",'grapes','apple']
    print(max(fruits))  -- output - orange

min() - gives the smallest object in the list
eg :fruits = ["apple", "banana", "orange",'grapes','apple']
    print(min(fruits))  -- output - apple

sorted() - returns a new list with objects arranged in ascending order
eg :fruits = ["apple", "banana", "orange",'grapes','apple']
    print(sorted(fruits))  -- output - ['apple', 'apple', 'banana', 'grapes', 'orange']

sort() - changes the original list




####################################################################################

## Interview Nuggets

- Lists are mutable, heterogenous and can be resized dynamically
- Arrays are homogenous oand often fixed size
- Tuples are immutable.
- Tuples are used as dictionary keys because they are immutable and hashable, allowing Python to efficiently locate data via a fixed hash value
- append() adds one item.
- extend() adds multiple items.
- remove deletes an item by its value.
- pop deletes by its index position  and returns that item
- sort() modifies the original list.
- sorted() returns a new list.
- reverse() reverses the current order; it does not sort.
- The core difference between reverse() and [::-1] in Python is that reverse() modifies the original list in-place and returns None, while [::-1] creates a brand-new copy of the object in reverse order
