favourite_places = {
    "Xan" : ['France','Paris','Ireland'],
    "else" : ['None']
}
for name,places in favourite_places.items():
    if len(places) > 1:
        print(name + "'s favouriter places are")
        for place in places:
            print(place)
    else:
        print(name + "'s favouriter place is ")
        print(places[0])