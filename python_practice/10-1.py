with open("learning_python",'w') as file_object:
    file_object.write("In python you can learn how to write a worm")
    file_object.write("\nIn python you can learn how to draw a picture")
    file_object.write("\nIn python you can learn how to be a hacker")
with open("learning_python",'r') as file_object:
    contents = file_object.read();          #read()函数读取文件的全部内容，在文件末尾时返回一个空字符串。
    print(contents)
lines =[]
with open("learning_python",'r') as file_object:
    lines = file_object.readlines()
for line in lines:
    try:
        if  'python' in line:
            print(line.replace('python','c'))
        else:
            print(line)
    except FileNotFoundError:
        print("Please enter right filepath")
