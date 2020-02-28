#ticket
'''
<3         Free
>3  <12    10
>12        15
'''
message = "OH,how old are you?\n"
active = True
while active:
    age = input(message)
    if age == 'quit':
        break
    age = int(age)
    if age <3 and age>=0:
        print("FREE!!!")
    elif age >=3 and age <=12:
        print("10$")
    elif age > 12:
        print("15$")
    else:
        print("Please input real age !")