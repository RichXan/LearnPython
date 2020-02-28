cities ={
    'Shanghai' : {
        'country' :'china',
        'population': '50million',
        'fact':'four destinctive seasons'
    },
    'HongKong' : {
        'country': 'china',
        'population':'3million',
        'fact':'very advanced in past but primitive now'
    },
    'Paris':{
        'country':'France',
        'population':'3million',
        'fact':'used to very advanced and now it is'
    }
}
for city ,information in cities.items():
    print("\n" +city + "'s information:")
    for fake ,real in information.items():
        print(fake + " : "+ real)