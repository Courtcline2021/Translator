import googletrans

languages = googletrans.LANGUAGES # stores languages 

for i in languages: # loops through and displays all langs
    print(i)


from_lang = input("Enter Starter Language:  ")
lang_choice = input("Enter what language you want to translate to:  ")

if languages == lang_choice:
    pass
else:
    print("Sorry Language Not Found")
    input("Enter Language: ")
    

f = open("mytranslator.txt", "x")
