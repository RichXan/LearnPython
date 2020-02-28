river_country = {"nile":"egypt",'niguer':'china','molihe':'raxier'}
for river , country in river_country.items():
    print("The " + river.title() + " runs through " + country.title())
for river in river_country.keys():
    print(river.title())
for country in river_country.values():
    print(country.title())