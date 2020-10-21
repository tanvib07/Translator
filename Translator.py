from googletrans import Translator
from tkinter import *

root = Tk()
root.geometry('680x700')
root.configure(bg='grey')
#variables

#option variable
optvar = StringVar()
text =StringVar()
OptionList = [
    'choose language','hindi','marathi','irish','italian','japanese','kannada','latin','malayalam','punjabi'

]
optvar.set(OptionList[0])

adlbl = Label(root, text='TRANSOLATOR', font=('Arial', 15), fg='purple')
adlbl.grid(row=0, column=0, sticky='n')

#get text from user
entr = Entry(font=('Arial', 23), fg='red', width=40, textvariable=text)
entr.grid(row=1, column=0, sticky='n', pady=13)

lbl1 = Label(root, text='Choose Which Language You Have To Translate ?', font=('Courier New', 15), bg='black',fg = 'white')
lbl1.grid(row=2, column=0, sticky='nw')

#option list
opt = OptionMenu(root, optvar, *OptionList)
opt.grid(row=3, column=0, pady=7)

def trans():
    ttext = text.get()
    optval = optvar.get()
    transolator = Translator()
    det = transolator.detect(ttext)
    #display detected language
    detlbl = Label(root, text=f'Detected Language Is : {det.lang}', font=('Arial', 15), fg='gray20')
    detlbl.grid(row=5, column=0, sticky='n')

    #translate language
    translated = transolator.translate(ttext, dest=optval)
    print(translated)

    #display the translated text
    t = Text(root, height=20, width=60)
    t.grid(row=6, column=0, sticky='nwe')
    tr = translated.text
    t.insert(INSERT, tr)
    
#button
btn = Button(text='TRANSLATE', font=('Arial', 20), fg='black',bg='light blue', command=trans)
btn.grid(row=4, column=0, sticky='n', pady=7)


root.mainloop()

