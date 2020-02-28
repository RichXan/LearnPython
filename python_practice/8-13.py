#形参**user_info中的两个星号是创建一个名为user_info的空字典，可以在定义函数时对形参进行初始化。
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的y一切"""
    profile = {}
    profile['first_name'] = first
    profile["last_name" ] = last
    for key ,value in user_info.items():
        profile[key] = value
    return profile
user_profile  = build_profile("Rich","Xan",
                              nowLeran = "Python",
                              usedLearn = "C",
)
print(user_profile)