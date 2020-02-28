def city_country(city,country):
    return '"'+city+ ","+ country+ '"'
sc = city_country("shenzhen".title(),"china".title())
print(sc)
demo2 = city_country("Paris","France")
print(demo2)
demo3 = city_country("Seoul",'Korea')
print(demo3)
