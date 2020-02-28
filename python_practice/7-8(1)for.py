sandwich_orders = ['A','pastrami','B','pastrami','C','D','pastrami','E']
while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches =[]
for sandwich in sandwich_orders:
    print("I made your " + sandwich +" sandwich.")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)