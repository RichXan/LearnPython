peoples_information = {
    "Xan" :{'first_name':'Rich',
                      'last_name':'Xan',
                      'age':15,
                      'city':'DongGuang'
                    },
    "Hamber" : {
                        'first_name' : 'wang',
                        'last_name' : 'weirang',
                        'age':20,
                        'city':'jiling'
                    },
    "Yang" : {
                    'first_name':'liu',
                    'last_name':'junqing',
                    'age':21,
                    'city':'fuzhou'
                    }
    }
for name , informations in peoples_information.items():
    print("\nThere are " + name + " informations :" )
    for fake,information in informations.items():
        print(fake + " : "+str(information))