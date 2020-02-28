current_users = ['AAA','BBB','CCC','DDD','EEE']
new_users = ['EEE','BBB','admin']
for user in new_users:
    if user in current_users:
        print("yess")
    else:
        print("nonoono")