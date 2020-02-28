# 形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组。
def make_pizza(*toppings):
    print("Making your pizza with:")
    for topping in toppings:
        print( "- "+topping)

def window(list):
    print("You can enter 'q' to quit in anytime")
    while True:
        top = input("Please print your topping: ")
        if top == 'q':
            break
        else:
            list.append(top)
def make_list_pizza(list):
    print("Making your pizza with : ")
    for topping in list:
        print("- "+ topping)

list =[]
window(list)
make_list_pizza(list)