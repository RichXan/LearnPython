users_name = ['admin','Eric','Mike','John','Michel']
if users_name:
    for user in users_name:             #为什么users_name == True的值为False
        if user == "admin":
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello "+ user + ",thank you for logging in again.")
else:
    print("We need to find some users!")