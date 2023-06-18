from tkinter import *
window = Tk()
window.geometry('300x400')




optionlist = [
    'hihihiha',
    'ocak',
    'şubat',
    'mart',
    'nisan',
    'mayıs',
    'haziran',
    'temmuz',
    'ağustos',
    'Eylül',
    'ekim',
    'kasım',
    'aralık'
]
photo = PhotoImage(file='hihihiha.png')

photo_resized = photo.subsample(1,1)



# sval = StringVar(value=optionlist[0])
sval =  StringVar()
sval.set(optionlist[0])


opm1 = OptionMenu(window, sval, *optionlist)

opm1.configure(font='Arial 15 bold', bg='red', fg='yellow', cursor='spider', anchor='sw',
               relief='sunken', image=photo_resized, compound=LEFT)
opm1.pack()


def clicked_button():
    print(sval.get())

Button(window,text='Bana tıkla!!', command=clicked_button).pack(pady=20)








window.mainloop()
