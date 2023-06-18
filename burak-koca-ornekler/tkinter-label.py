from tkinter import *

# text
# font
# bg
# fg
# cursor
# height - KAÇ SATIR
# width - KAÇ HARF
# wraplenght
# padx
# pady
# anchor
# relief (FLAT-RAISED-SUNKEN-GROOVE-RIDGE)
# bitmap
# image
# compound

window = Tk()
window.geometry('400x400')

# Label(window, text='pyton tk label', font=('Helvetica 30 bold underline italic ')).pack()
# Label(window, text='pyton tk label', font=('arial 20')).pack()

# Label(window, text='python tk label', font=('times', 15,), bg='green', fg='red', cursor='heart',
#       height=8, width=10, wraplength=20).pack()


# PADX PADY
# Label(window, text='pyton tk label', font=('arial', 30), bg='green').pack()
# Label(window, text='pyton tk label', font=('arial', 30), bg='green', padx=20, pady=20).pack()

# ANCHOR
# Label(window, text='label', font=('Arial', 20), width=15, height=8, bg='red').pack()
# Label(window, text='label', font=('Arial', 20), width=15, height=8, bg='red', anchor='sw').pack()


# RELİEF
# Label(window, text='label', font=('Arial', 20), relief=FLAT).pack()
# Label(window, text='label', font=('Arial', 20), relief=RAISED).pack()
# Label(window, text='label', font=('Arial', 20), relief=SUNKEN).pack()
# Label(window, text='label', font=('Arial', 20), relief=GROOVE).pack()
# Label(window, text='label', font=('Arial', 20), relief=RIDGE).pack()

# BİTMAP
# Label(window, bitmap='error').pack()
# Label(window, bitmap='gray25').pack()
# Label(window, font=('arial 20'), bitmap='question').pack()

# İMAGE
photo = PhotoImage(file='hihihiha.png')
photoresized =  photo.subsample(3, 3)

Label(window, text='HİHİHİHA', font=('arial 30'), image=photo, compound=LEFT).pack()

# Label(window, text='pyton tk label', font=('arial 20'), image=photoresized).pack()







window.mainloop()