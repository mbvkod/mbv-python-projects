from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry('400x300')




def clicked_button():
    # responce = messagebox.showinfo('show info', 'info')
    # print(responce)

    # responce = messagebox.showwarning('show warning', 'warning')
    # print(responce)

    # responce = messagebox.showerror('show error', 'eroror')
    # print(responce)

    # responce = messagebox.askquestion('question', 'are you sure')
    # print(responce)

    # responce = messagebox.askokcancel('ok cancel', 'Do you want to continue')
    # print(responce)

    # responce = messagebox.askretrycancel('rety cancel', 'are you sure')
    # print(responce)

    # responce = messagebox.askyesno('yes no', 'are you sure')
    # print(responce)

    responce = messagebox.askyesnocancel('yes no cancel', 'are you sure')
    print(responce)




Button(window, text='click me!', command=clicked_button).pack()








window.mainloop()