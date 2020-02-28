sandwich_orders = ['A','pastrami','B','C','pastrami','D','E','pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches =[]
active = True
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
    print("I made your " +current_sandwich+ " sandwich")
print(finished_sandwiches)