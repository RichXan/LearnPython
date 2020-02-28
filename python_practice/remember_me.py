import json
filename = "user_name.json"
try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("Please enter your name : ")
    with open(filename,'w') as file_object:
        json.dump(username,file_object)
        print("We will welcome you next time.")
else:
    print("Welcome back!! " + username)