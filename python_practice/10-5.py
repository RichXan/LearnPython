print("you can print 'q' to quit")
lists =[]
while True:
    list = input("Enter why you like python: ")
    if list == 'q':
        break
    lists.append(list)
print(lists)
try:
    with open("like_python_reason.txt",'w+') as file_object:
        for list1 in lists:
            i = list1 + '\n'
            file_object.write(i)
        for line in file_object:                            # 读写文件这两个步骤要分开么？？？？？
            print(line)
except FileNotFoundError:
    print("file not found".title())