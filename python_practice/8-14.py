def car_information(manufacturer,type,**infos):
    alist={}
    alist["manufacturer"]= manufacturer
    alist["type"] = type
    for key,value in infos.items():
        alist[key]= value
    return alist
mycar = car_information('subaru','outback',
                        color = 'blue',
                        tow_package = True
                        )

print('---------------------------------------------------------------------------------------')
print(mycar)
print('---------------------------------------------------------------------------------------')

