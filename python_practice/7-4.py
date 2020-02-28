message = "please enter your dosing of pizza:"
message+= "\n Enter 'quit' to quit.  "
print(message)
active = True
while active:
    dosing = input()
    if dosing  == 'quit':
        break
    else:
        print("We will add this dosing!")