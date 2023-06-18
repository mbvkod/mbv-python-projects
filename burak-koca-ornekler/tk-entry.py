from tkinter import *
window = Tk()
window.geometry('400x400')
# Entry(window, ).pack()
# Entry(window, font='Arial 14 bold underline', bg='red', fg='blue', border=5, width=10, cursor='spider', relief='').pack()


# Entry(window, relief=FLAT).pack(pady=10)
# Entry(window, relief=RAISED).pack(pady=10)
# Entry(window, relief=SUNKEN).pack(pady=10)
# Entry(window, relief=GROOVE).pack(pady=10)
# Entry(window, relief=RIDGE).pack(pady=10)


# Entry(window, show='0').pack()


# Entry(window, justify='right').pack()


# Entry(window, selectbackground='yellow', selectforeground='red', selectborderwidth=5).pack()


# Entry(window, ).pack(pady=20)
# Entry(window, state='disabled').pack(pady=20)


# svar = StringVar(window, value='bumbumtamtam')
# Entry(window, textvariable=svar).pack()



ent1 = Entry(window, width=40   )
ent1.pack(pady=10)


def clicked_button():
    # ent1.insert(2, '0')
    # print(ent1.get())

    # ent1.delete(1, 2)
    # ent1.delete(0, 'end')

    # ent1.select_to(2)
    # ent1.select_range(3, 6)
    # print(ent1.select_present())
    ent1.icursor(4)


Button(window, pady=10, text='Click me!', command=clicked_button).pack(pady=10)







window.mainloop()