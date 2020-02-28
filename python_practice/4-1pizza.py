pizzas = [' bishengke',' kfc',' jingongmeng']
for pizza in pizzas:
    print("I like "+ pizza.lstrip() + " pizza")
print("I really like eating pizza ecepially " + pizzas[0] + pizzas[1] + pizzas[2] +" pizza.I really love pizza")
friend_pizzas = pizzas[:]
pizzas.append("hbb")
friend_pizzas.append("hollllll")
print("My favorite pizzas are:")
for pizza in pizzas :
    print(pizza)
print("My friend favorite pizzas are:")
for pizza in friend_pizzas :
    print(pizza)