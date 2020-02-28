def make_album(musician,album_name,numbers = 1):
    albums ={'musician':musician,
             'album name':album_name
    }
    if numbers != 1:
        albums['numbers'] = numbers
    return albums
while True:
    print("(enter 'q' at any time to quit)")
    musician = input("Please enter a musician name : ")
    if musician == 'q':
        break
    album_name = input("Please enter a album name : ")
    if album_name == 'q':
        break
    numbers = input("Enter the number of the album : ")
    if numbers == 'q':
        break
    dics = make_album(musician,album_name,numbers)
    print(dics)