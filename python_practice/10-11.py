import json

'''接受用户输入的最喜欢的数字
然后用json.dump（）存储到文件中
再读取文件输出
'''
def loaddata(filename):
    with open(filename) as file_object:
        fnumber = json.load(file_object)
        return fnumber

def dumpdata(filename):
    number = input("Please input your favourite number : ")
    with open(filename, 'w') as  file_object:
        json.dump(number, file_object)

def printdata(fnumber):
    print("I konw your favourite number .Hahhhhhh")
    print("It is " + fnumber + "!!!")

while True:
    filename = "number.json"
    try:
        fnumber = loaddata(filename)

    except FileNotFoundError:
        dumpdata(filename)
        continue

    else:
        printdata(fnumber)
        break