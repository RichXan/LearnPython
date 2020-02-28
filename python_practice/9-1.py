'''创建Restaurant类包含初始化，餐厅描述，餐厅营业方法。'''
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The name of restaurant is " + self.restaurant_name )
        print("And the cuisine type is " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name + "is openning !!!")
        print("Welcome to "+self.restaurant_name)
my_restaurant = Restaurant("RichFood","CantoneseFood")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
xan_restaurant = Restaurant("Xan",'CHUANG')
ziqiao_restaurant = Restaurant("LilQiao",'CHUANCANTONESE')
xan_restaurant.describe_restaurant()
ziqiao_restaurant.describe_restaurant()