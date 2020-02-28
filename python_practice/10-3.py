'''写一个顾客把自己名字的输入，然后存储到一个文件当中'''
with open("custom_name.txt",'w') as file_object:
    print('you can enter "q" to quit at anytime!!!')
    while True:
        name  = input("Please enter your name:")
        if name  !=  'q':
            file_object.write(name+'\n')
        else:
            break

try:
    with open("custom_name.txt",'r') as file_object:
        names = file_object
        for i in names:
            print(i)
except ValueError:
    print("Something error")