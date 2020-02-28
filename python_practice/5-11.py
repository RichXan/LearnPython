number_list = [number for number in range(1,10)]
for number in number_list:
    print(number,end="")        #打印不换行
    if number==1:
        print("st")
    elif number ==2:
        print("nd")
    elif number ==3:
        print("rd")
    else:
        print("th")