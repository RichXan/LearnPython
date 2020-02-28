car  = 'BMW'
print("car is " + car)
print("car == 'Bmw';" )
print(car == 'Bmw')         #false
print("car == 'bmw':")
print(car == car.lower())   #false
print("car == car:")
print( car == car)          #true
print("car != car:")
print(car != car)           #false
print("car > car:")
print(car > car)            #false
print("car < car:")
print(car < car)            #false
print("car >= car:")
print(car >= car)           #true
print("car <= car:")
print(car <= car)           #true
my_car = ['bwm','benchi','biyadi']
if 'bwm' in my_car:
    print("Yepppp")
else:
    print("NOOOOO")
