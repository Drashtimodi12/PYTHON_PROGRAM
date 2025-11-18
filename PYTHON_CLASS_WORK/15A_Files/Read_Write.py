# Read and Write in "w+" Mode
# "w+" mode writes to the file and allows reading after writing.
# It overwrites the file if it already exists.

with open("Test.txt", "w+") as file:
    file.write("Hello PYTHON")  # Write to file
    file.seek(0)  # Move cursor to the beginning, seek(0) moves the cursor to the start of the file before reading
    a = file.read()  # Read the file content
    print(a)

# Output:
# Test.txt ---Create new file and write
# Hello PYTHON