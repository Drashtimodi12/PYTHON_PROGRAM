# Writing to a File ("w" mode)
# The "w" mode creates a new file or overwrites an existing file.
# If the file exists, its content is deleted before writing new data.


file = open("Test.txt", "w")        # Open a file in write mode
file.write("Python Program\n")      # Write data to the file
file.close()                        # Close the file to save changes

# Output:
# Test.txt --- Create File
# Python Program
