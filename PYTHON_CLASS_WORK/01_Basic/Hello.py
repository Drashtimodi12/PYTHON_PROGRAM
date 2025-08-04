# Open Terminal Press Ctrl + ~
# Check the directory where your file is saved.
# Use the cd command to change directories. cd .\Basic\
# Ex: cd C:\PYTHON_PROGRAM\PYTHON_CLASS_WORK\Basic
# If you need to move back a folder, use: cd ..
# Run: Once you're inside the correct folder, run the program with:  py .\Hello.py

# Printing simple text messages
print ('1. Hello Python')  # Single quotes
print("2. Hello Python!")  # Double quotes

# Printing multi-line string
print("""3. Hello Everyone!
Wellcome""")

# Printing with single and double quotes inside the string
print("4. Hello ' Python! '")   # Single quotes inside double quotes
print('5. Hello " Python! "')   # Double quotes inside single quotes

# Using escape characters to include quotes
print("6. Hello \" Python! \"")    # Escaping double quotes
print('7. Hello \' Python! \'')    # Escaping single quotes

# Using escape characters to include backslashes
print("8. Hello \\ Python! \\")    # Escaping backslashes

# Printing with special characters
print("9. Hello \ Python! \ ")     # Single backslash before spaces
print("10. Hello \n Wellcome")      # New line character
print("11. Hello \t Wellcome")      # Tab space
print("12. Hello!\b Python!")       # Backspace
print("13. Hello \\\" Python! \"")  # Escaping backslash and double quotes

# Print with end and separator
print("14. hello",end=" ")  # Prints 'hello' without a newline, adding a space instead
print("python")     # Output: hello python

print("16. python","java","php","node",sep=" ")     # Prints with space separator, Output: python java php node
print("17. python","java","php","node",sep=" | ")   # Prints with '|' separator, Output: python | java | php | node