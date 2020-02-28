huangtuotuo = {
            "master":"sister",
            "kind":"cat"
    }
xiaohei  = {
            "master":"Xan",
            "kind":'dog'
    }
pets = [huangtuotuo,xiaohei]
for pet in pets :
    print( "\n"+  +"'s information:")        #如何打印存储字典的列表中的字典名
    for key,value in pet.items():
        print(key + " ; "+ value)
