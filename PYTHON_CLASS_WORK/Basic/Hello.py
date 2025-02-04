# Open Terminal Press Ctrl + ~
# Check the directory where your file is saved.
# Use the cd command to change directories. cd .\Basic\
# Ex: cd C:\PYTHON_PROGRAM\PYTHON_CLASS_WORK\Basic
# If you need to move back a folder, use: cd ..
# Run: Once you're inside the correct folder, run the program with:  py .\Hello.py

# Printing simple text messages
print ('Hello Python')  # Single quotes
print("Hello Python!")  # Double quotes

# Printing multi-line string
print("""Hello Everyone!
Wellcome""")

# Printing with single and double quotes inside the string
print("Hello ' Python! '")   # Single quotes inside double quotes
print('Hello " Python! "')   # Double quotes inside single quotes

# Using escape characters to include quotes
print("Hello \" Python! \"")    # Escaping double quotes
print('Hello \' Python! \'')    # Escaping single quotes

# Using escape characters to include backslashes
print("Hello \\ Python! \\")    # Escaping backslashes

# Printing with special characters
print("Hello \ Python! \ ")     # Single backslash before spaces
print("Hello \n Wellcome")      # New line character
print("Hello \t Wellcome")      # Tab space
print("Hello!\b Python!")       # Backspace
print("Hello \\\" Python! \"")  # Escaping backslash and double quotes

# Print with end and separator
print("hello",end=" ")  # Prints 'hello' without a newline, adding a space instead
print("python")     # Output: hello python

print("python","java","php","node",sep=" ")     # Prints with space separator, Output: python java php node
print("python","java","php","node",sep=" | ")   # Prints with '|' separator, Output: python | java | php | node