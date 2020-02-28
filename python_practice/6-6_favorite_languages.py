favourite_languages ={
    'jen':'python',
    'sarah':'c',
    'edward': 'ruby',
    'phil':'python',
    }
survey_peoples =['jen','phil','peter','mike']
for people in favourite_languages.keys():
    if people in survey_peoples:
        print("Thank you " + people.title() + " to join my investigated")
    else:
        print("Oh " + people.title() + " !Can you join my investiage")
