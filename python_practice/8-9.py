
def show_magicians(Magicians_name):
    print("================")
    for magician in Magicians_name:
        print(magician.title())
def make_great(Magicians_name1,Magicans_name2):             #歌手名前加The Great
    while Magicians_name1:
        Magicians = Magicians_name1.pop()
        Magicians = "The Great " + Magicians
        Magicans_name2.append(Magicians)

magicians = ["java", 'python', 'c']
made_magicians = []
show_magicians(magicians)
make_great(magicians[:],made_magicians)
show_magicians(made_magicians)
show_magicians(magicians)