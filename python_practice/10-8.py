try:
    with open('cat.txt','w') as file_object:
        file_object.write("A")
        file_object.write("B")
        file_object.write("C")

    with open('dog.txt','w') as file_object:
        file_object.write("D")
        file_object.write("E")
        file_object.write("F")

    with open('cat.txt','r') as file_object:
        contents = file_object.read()
        print(contents)

    with open('dog.txt', 'r') as file_object:
        contents = file_object.read()
        print(contents)

    with open("copydog.txt",'w') as file_object:
        file_object.write(contents)

    with open('copydog.txt', 'r') as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError:
    print("The file is not found...")
    #or
    #pass
