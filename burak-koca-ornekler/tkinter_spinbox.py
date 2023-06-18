from tkinter import *
window = Tk()
window.geometry('400x300')




sval = IntVar(value=18)

def changed_value():
    print(spb1.get())


spb1 = Spinbox(window, from_=1, to=100, increment=5, font='Times 15 bold', bg='red', fg='blue', cursor='dotbox',
        bd=7, width=30, justify='center', relief=RIDGE, state='normal', textvariable=sval,
        command=changed_value)

spb1.pack()


Spinbox(window, from_=1, to=100, increment=5, font=('Times 15 bold'), bg='red', fg='blue', cursor='dotbox',
        bd=7, width=30, justify='center', relief=RIDGE, state='disabled', disabledbackground='gray',
        disabledforeground='black').pack()




window.mainloop()
