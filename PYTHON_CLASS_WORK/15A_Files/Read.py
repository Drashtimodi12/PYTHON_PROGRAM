# Reading from a File ("r" mode)
# The "r" mode is used to read content from a file.
# If the file does not exist, an error occurs.

# file = open("Test.txt", "r")  # Open file in read mode
# content = file.read()  # Read file content
# print(content)  # Print content
# file.close()  # Close file

# Output:
# Test.txt --- Read File
# Python Program



# Reading Line by Line (readline())
# Reads file one line at a time in a loop.
# Stops when no more lines are available.

# file = open("Test.txt", "r")  # Open file in read mode
# while True:
#     line = file.readline()  # Read one line
#     if not line:  # Break loop if end of file
#         break
#     print(line)  # Print without extra new lines
# file.close()  # Close file

# Output:
# Test.txt ---Read line by line File
# Python Program
# 
# Java Program
# 




# Reading All Lines at Once (readlines())
# Reads all lines and returns them as a list of strings.

file = open("Test.txt", "r")  # Open file in read mode
lines = file.readlines()  # Read all lines as a list
print(lines)  # Print list of lines
file.close()  # Close file

# Output: 
# Test.txt ---File Read and Print as a List
# ['Python Program\n', 'Java Program\n']









# -----------------------------
# Image Read
# -----------------------------

# # Open the file "BG_12.jpg" in binary read mode ('rb')
# with open("BG_12.jpg",'rb') as f:
#     reader = f.read()   # Read the content of the file into the variable 'dt'
#     print(reader)        # Print the binary content of the file (which will appear as a sequence of bytes)
# # The program will likely fail or return incorrect data, because image files contain non-text characters.