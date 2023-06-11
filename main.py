
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title('Language Translator')
root.geometry('870x320')
root.configure(bg='#C4DFDF')

primary_color = 'black'
secondary_color = '#E3F4F4'

def translate():
    translated_text.delete(1.0, END)

    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                 original_key = key

        for key, value in languages.items():
            if (value == translate_combo.get()):
                 translated_key = key

        words = textblob.TextBlob(original_text.get(1.0,END))

        words = words.translate(from_lang = original_key , to = translated_key)

        translated_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator",e)


def interchange():  
    original_value = original_combo.get()
    translate_value = translate_combo.get()

    original_combo.set(translate_value)
    translate_combo.set(original_value)

    original_text_value = original_text.get(1.0,END)
    translated_text_value = translated_text.get(1.0,END)

    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)

    original_text.insert(1.0, translated_text_value)
    translated_text.insert(1.0, original_text)
    
def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)

languages = googletrans.LANGUAGES
language = list(languages.values())

original_text = Text(root, height=10,width=40)
original_text.grid(row=0,column=0,padx=10,pady=20)

translate_button = Button(root,text='Translate', font=("Times New Roman",24),command=translate,bg=secondary_color, fg=primary_color)
translate_button.grid(row=0,column=1,padx=5)

interchange_button = Button(root,text="< -- >",font=("Times New Roman",12),command=interchange,bg=secondary_color, fg=primary_color)
interchange_button.grid(row=1,column=1,padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0,column=2,padx=10,pady=20)

original_combo = ttk.Combobox(root,width=50, value= language)
original_combo.current(5)
original_combo.grid(row=1, column=0)

translate_combo= ttk.Combobox(root,width=50, value= language)
translate_combo.current(5)
translate_combo.grid(row=1, column=2)

clear_text = Button(root,text="Clear",font=("Times New Roman",16),command=clear,bg=secondary_color, fg=primary_color)
clear_text.grid(row=3,column=1, padx=15)

root.mainloop()