'''创建User类，包含初始化，描述用户，欢迎用户方法'''
class User:
    def __init__(self,first_name,last_name,*otherinfo):
        self.first_name = first_name
        self.last_name = last_name
        for info in otherinfo:
            print("- "+ info)

    def decribe_user(self):
        print("NOthing")
    def greet_user(self):
        print("WDNMD \nHOW ARE U?")
        print("I AM VRRY FINE.")

xan = User("Rich",'Xan','I','AM','Very','RICH')
xan.decribe_user()
xan.greet_user()