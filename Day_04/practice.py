# 1.Create a list of five fruits.
#Print -entire list, first element, last element
fruits = ["apple", "banana", "litchi",'grapes','jackfruit']
print(fruits)
print(fruits[0])
print(fruits[-1])

# 2.add 'mango' to the list
fruits.append('Mango')

# 3.Insert 'Orange' at index 2
fruits.insert(2,'Orange')

# 4.Remove 'banana' from the list.
fruits.remove('banana')

# 5.Print the length of the list.
print(len(fruits))

#6. Find the largest number without using max()
numbers = [15,3,21,8,19]
largest = numbers[0]
for i in numbers:
    if i>largest:
        largest = i
print(largest)

#7. Find the smallest number without using min()
numbers = [15,3,21,8,19]
smallest = numbers[0]
for i in numbers:
    if i<smallest:
        smallest = i
print(smallest)

#8. Reverse a list using a loop without using [::-1], reverse()  (did'nt solve)
numbers = [15,3,21,8,19]
rev_numbers = []
for i in range(len(numbers)-1,-1,-1):
    rev_numbers.append(numbers[i])
print(rev_numbers)

#9. Remove duplicate elements.
lst = [1,2,2,3,4,4,5]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)

print(new_lst)

#10.Find the second largest number. 
numbers = [15, 3, 21, 8, 19]

largest = numbers[0]
second_largest = numbers[0]

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)

# 11.How would you swap the first and last elements of a list?
lst = [10,20,30,40]
lst[0],lst[-1] = lst[-1],lst[0]
print(lst)
