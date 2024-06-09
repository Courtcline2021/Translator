from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator


root = Tk()
root.geometry('1100x320')
root.resizable(0,0)
root['bg'] = 'yellow'
root.title('Translator')

Label(root, text='Language Translator', font='Arial 20 bold').pack()
Label(root, text='Enter Text', font='arial 13 bold', bg='white smoke').place(x=165,y=90)

Input_text= Entry(root, width=60)
Input_text.place(x=30, y=130)

Label(root, text='Output', font='arial 13 bold', bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 10', height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=130, y=180)
dest_lang.set('Pick a Language')

def Translate():
    try:
        translator = Translator(dest_lang.get())
        translation = translator.translate(Input_text.get(), dest=dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END, translation.text)
    except Exception as e:
        print(f"Translation error: {e}")

trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='pink', activebackground='light grey')  
trans_btn.place(x=445, y=180)

root.mainloop()


#languages = googletrans.LANGUAGES # stores languages 

#for i in languages: # loops through and displays all langs
    #print(i)


#from_lang = input("Enter Starter Language:  ")
#lang_choice = input("Enter what language you want to translate to:  ")

#if languages == lang_choice:
    #pass
#else:
 #   print("Sorry Language Not Found")
  #  input("Enter Language: ")