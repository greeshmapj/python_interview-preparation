#Create a file named sample.txt inside the folder.


#1. Read the entire file.
file = open("Python/Day_07/sample.txt","r")
print(file.read())
file.close()

# 2. Print the file line by line.
with open("Python/Day_07/sample.txt","r") as f:
    for line in f:
        print(line)

# 3. Count the number of lines.
with open("Python/Day_07/sample.txt","r") as f:
    line_count = sum(1 for line in f)
print(line_count)

# 4. Count the total number of words.
with open("Python/Day_07/sample.txt","r") as f:
    count = 0
    for i in f:
        count += len(i.split())
    print(count)

# 5. Append 'Data Science' to the file.
with open("Python/Day_07/sample.txt","a") as f:
    f.write('\nData Science')

# 6. Create a new file 'copy.txt' and copy everything from sample.txt into it. 
with open("Python/Day_07/sample.txt","r") as source, open('Python/Day_07/copy.txt','w') as dest:
    dest.write(source.read())

# 7. Find the longest line in the file.
with open("Python/Day_07/sample.txt","r") as f:
    lines = f.readlines()
    longest = lines[0]
    for i in lines:
        if len(i) > len(longest):
            longest = i
    print(longest)

# 8. Count how many times the word "Learning" appears.
with open("Python/Day_07/sample.txt","r") as f:
    count = 0
    for i in f:
        count += i.count("Leaning")
    print(count)

# 9. Convert the entire file contents to uppercase and save it as 'uppercase.txt'
with open("Python/Day_07/sample.txt","r") as src, open("Python/Day_07/uppercase.txt","w") as dest:
    dest.write(src.read().upper())

# 10. Print only the lines that contain "Python".
with open("Python/Day_07/sample.txt","r") as f:
    for lines in f:
        if "Python" in lines:
            print(lines)


#TasK 3 - Debugging

#Debug 1
file = open("Python/Day_07/sample.txt","r")
print(file.read())
file.close()

#Debug 2
with open("Python/Day_07/sample.txt","r") as file:
    print(file.read())

#Debug 3
file = open("Python/Day_07/sample.txt","a")
file.write("Hello")
file.close()
# we cannot do write operation in read mode.
      
        


        
     

   


