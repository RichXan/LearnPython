message = "If you could visit one place in the world,where would you go?\n"
active = True
places = []
print("Enter 'quit' to quit")
while active:
    place = input(message)
    if place == 'quit':
        active = False
        break
    places.append(place)
print(places)
