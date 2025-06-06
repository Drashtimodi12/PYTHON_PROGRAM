# Copy a Dictionary:- You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference 
# to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
mydict = student.copy()
print(mydict)       # Output: {'Name': 'Drashti', 'Age': 21, 'Add': 'Surat', 'Contact': 9909449049}


# Another way to make a copy is to use the built-in function dict().
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
mydict = dict(student)
print(mydict)       # Output: {'Name': 'Drashti', 'Age': 21, 'Add': 'Surat', 'Contact': 9909449049}