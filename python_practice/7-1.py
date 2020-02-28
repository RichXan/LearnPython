#  7-1
car = input("Which car would you like to rent? ")
print("Let me see if I can find you a "+ car)

#  7-2
people  = input("How many peoples do you hava? ")
people = int(people)
if people >8:
    print("Sorry,we don't have such big table.")
else:
    print("This way,please.")

#   7-3
number = input("Please input a number as you like. ")
number = int(number)
if number%10 == 0:
    print("a multiple of ten")
else:
    print("is not a multiple of ten")