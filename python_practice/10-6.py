'''尝试将用户提供的两个输入 转换成整数，并进行加法运算
若不是整数，引发ValueError异常。并打印友好的异常提醒
'''
while True:
    i = input("Please input a number:")
    j = input("Please input a number:")
    try :
        i = int(i)
        j = int(j)
    except ValueError:
        print("u can't enter string ,u should enter a number")
        print("Please enter again")
        continue
    else:
        result = i+j
        print("your two numbers add result is " + str(result))
        break