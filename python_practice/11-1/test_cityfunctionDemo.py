from city_functions import get_city_country
import unittest
print("You can quit at anytime")
print("If you wanna quit please enter 'q'")
while True:
    city = input("Please enter your city:")
    if city == 'q':
        break
    country = input("Please enter your country:")
    if country == 'q':
        break
    message = get_city_country(city,country)
print(message)
