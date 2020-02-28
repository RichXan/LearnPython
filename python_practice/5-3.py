color_list = ['red','green','yellow']
alien_color = 'red'
for alien_color in color_list:
    if alien_color == 'green':
        print("That alien is green and you rewarded 5 points")
    elif alien_color =='yellow':
        print("That alien is yellow and you rewarded 10 points")
    else:
        print("That alien is red and you rewarded 15 points")
