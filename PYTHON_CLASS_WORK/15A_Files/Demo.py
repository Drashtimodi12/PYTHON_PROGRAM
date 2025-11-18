



with open("Text.txt", "w+") as file :
    file.write("\n      Hello PYTHON")
    file.seek(0)
    a = file.read()
    print(a)



