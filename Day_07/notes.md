FILE HANDLING

1. What is File Handling?
Why file handling is used
Real-world examples
File handling is the process of creating, opening, reading, writing, updating, and closing files stored on a computer.
eg: system logs, automated data like for ecommerce website, saving the profile picture in social platforms.

2. File Modes
Explain with one example each:
r - to read the data from file, cursor in beginning and if the file diesn't exist throws an error.
f = open("file_name","r")
data = f.read()
print(data)

w - to write into file, cursor in beginning and if the file diesn't exist creates a new file and overwrites the file for previously existing file.
f = open("file_name","w")
data = f.write("Hi All")

a - the write into file at the end of the existing data.f the file diesn't exist creates a new file and overwrites the file for previously existing file.
f = open("file_name","a")
data = f.write("Hi All") 

x - used to create a new file
f = open("file_name","x")

r+ - used for read and write operation. 
f = open("file_name","r+")
data = f.write("Hi All")

w+ - used for write and read operation
f = open("file_name","w+")
f.write("Hi All")
f.seek(0)
print(f.read())
f.close()

3. Common File Methods
Explain:

open() - used to open the file to perform the mode of operations
close() - used to close the file after doing the tasks
read() - used to read the data from the file
readline() - used to read one single line from the data and return it as string
readlines() - used to read the entire data as list of lines.
write() - used to write data into the file
writelines() - used to write multiple lines at once to the file.
seek() - used to bring the cursor to the desired location
eg: f = open("my_file","w+")
f.write("hiiiiiiiiiii")
f.seek(0)
f.read()
tell() - used to find the cursor location

4. Why use with open()?
Explain why it is preferred over manually calling close().
with open() helps to automatically close the file once the code completes executing or even if the code encounters an unhandled exception, preventing resorce leakage and data corruption. So we do not have to manually write the code to close the file and it even takes care of the situation of an unexpected error during coding.

5. . Interview Differences
read() vs readline() vs readlines() - 
read returns the entire data in the file as a single string
readline() - used to read one single line from the data and return it as string
readlines() - used to read the entire data as list of lines.

w vs a
w - Starts writing from beginning, deletes old content
a - Starts writing from end, keeps old content

write() vs writelines()
write() - used to write data into the file at any desired location
writelines() - used to write multiple lines at once to the file by including \n.
file.writelines(["AI\n","ML\n"])