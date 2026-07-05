1. What is a function?
A function is a reusable block of code that performs a specific task. It helps reduce code duplication and improves readability. 
for eg : the purpose of print fn is to display the output.

2. Why do we use functions?
we use functions to complete specific tasks with reduced code duplication, better readability & easier debugging. 
for eg: in real life washning machine is function and its prupose is to wash clothes

3. Syntax of a function 
def function_name(parameters):
    # code
eg: def greet():
    print("Hello")


4. Parameters
Parameters are variables written in the function definition.
eg: class add(5,7)
        print('hello') 
Here 5 and 7 are parameters.

Arguments - add is the argument here


5. Return vs Print - return does does not display the output, it keeps the output in its memory for later use. Where as print display the output

6. Local variable vs Global variable
Local variables are variable defined within that particular function, class, etc and can be used only within them locally.
Global variable can be used anywhere within the program. 
eg : here name is a global variable
name = "Greeshma"
def hello():
    print(name)

7. Types of functions
Built-in functions
these are automatically created by Python and can be used anywhere globally within the program. the programmer need not create it.
eg: print, type, lower, upper,etc
User-defined functions
these are manually created by the user depending on their requirement to satisfy the conditions 

8. Common built-in functions
len() - calculate the length
len('apple') = 5
type() - calculate the data type
type(8) - int
input() - user can provide the input
input('enter a number: ') = 9
print() - displays the output
print('mary') = mary
range() - series of sequence to be considered
range(1,4) = 1,2,3
sum() - calculates the sum
a = [1,2]
sum(a) = 3
max() - returns the largest element
max('apple') - p
min() - gives the smallest element
min('baby') - 'a'
