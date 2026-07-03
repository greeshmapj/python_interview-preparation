DECISION MAKING
if, else , elif - these are decision-making statements that allow a program to execute different blocks of code based on whether a condition is True or False.
for eg: 
if (x>0):
    print('positive number')
elif (x<0):
    print('negative number')
else:
    print('it is zero')

nested if - as the name suggest if we have multiple if-else within if-else then we call it nestedd if.
eg:
if (x>0):
    if (x%2==0):
        print('positive and multiple of 2')
    else:
        print('not a multiple of 2')
else:
    print('negative number')

LOOPS
for loop - A for loop is used to iterate over a sequence such as a list, tuple, string, or range.
eg:
for i in range(1,11):
    print(i)

while loop - can be used to apply a given condition for a sequence of numbers in range when the no.of iterations required is unknown and depends on dynamic condition
for eg:
i = 1
while i<=5:>
    print(i,"*")
    i+=1

range() - generates a sequence of mumbers. it can be used for loops.
for eg:if we have range(1,10) that means the given condition need to applied for numbers 1 to 9 as the second digit in range is (last number+1).

break - used to terminate the nearest loop
for i in range(5):
    if i == 3:
        break 
    print(i)

continue - continue skips the remaining statements in the current iteration and moves to the next iteration of the loop.
for i in range(5):
    if i == 2:
        continue
    print(i)

pass - its just the null statement in python used to fill when nothing happens or when we have intention to fill the condition at later stage.
for eg:
for i in range(10):
    pass



