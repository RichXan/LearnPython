favourite_numbers = {
    "Xan":[13,8],
    "Xufen":[7],
    "Hamber":[7]
}
for name ,numbers in favourite_numbers.items():
    if len(numbers)>1:
        print(name + "'s favourite numbers are :")
        for number in numbers:
            print(number)
    else:
        print(name + "'s favourite number is ")
        print(numbers[0])