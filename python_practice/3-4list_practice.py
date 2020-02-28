invited_name = ['kobe','jordon','k.n.g']
print(invited_name)
message1 = "Hello "+ invited_name[0].title() + " ! Could you have a dinner with me?"
print(message1)
message2 = "Hello "+ invited_name[1].title() + " ! Could you have a dinner with me?"
print(message2)
message3 = "Hello "+ invited_name[2].title() + " ! Could you have a dinner with me?"
print(message3)

print("\nOh!damn it.Sorry to heard that "+invited_name[0]+ " just gone...\n So he can't come." )
invited_name[0]='jj'
message1 = "Hello "+ invited_name[0].title() + " ! Could you have a dinner with me?"
print(message1)
message2 = "Hello "+ invited_name[1].title() + " ! Could you have a dinner with me?"
print(message2)
message3 = "Hello "+ invited_name[2].title() + " ! Could you have a dinner with me?"
print(message3)

print("\nhahhhhh.".title()+"I find a big table,I would invite more three people")
invited_name.insert(0,'professor')
invited_name.insert(2,'bone_collecter')
invited_name.append('xxx')
message1 = "Hello "+ invited_name[0].title() + " ! Could you have a dinner with me?"
print(message1)
message2 = "Hello "+ invited_name[1].title() + " ! Could you have a dinner with me?"
print(message2)
message3 = "Hello "+ invited_name[2].title() + " ! Could you have a dinner with me?"
print(message3)
message4 = "Hello "+ invited_name[3].title() + " ! Could you have a dinner with me?"
print(message4)
message5 = "Hello "+ invited_name[4].title() + " ! Could you have a dinner with me?"
print(message5)
message6 = "Hello "+ invited_name[5].title() + " ! Could you have a dinner with me?"
print(message6)

print("\nohh!nothing could be perdictd,the table can't be sent in time.Only two people could be invited to have dinner with me.")
whocantbeinvited=invited_name.pop()
print("Sorryyyyy."+whocantbeinvited)
whocantbeinvited=invited_name.pop()
print("Sorryyyyy."+whocantbeinvited)
whocantbeinvited=invited_name.pop()
print("Sorryyyyy."+whocantbeinvited)
whocantbeinvited=invited_name.pop()
print("Sorryyyyy."+whocantbeinvited)
print("\n"+invited_name[0]+' Could you have a dinner with me?')
print("\n"+invited_name[1]+' Could you have a dinner with me?')
del invited_name[0]
del invited_name[0]
print(invited_name)