from tkinter import *

window = Tk()

window.geometry('500x500')
window.configure(bg='black')

label1 = Label(window, text='label1')
label2 = Label(window, text='label2')
label3 = Label(window, text='label3')



# PACK

# label1.pack()
# label2.pack()
# label3.pack()


# GRİD

label1.grid(column=1, row=0)
label2.grid(column=2, row=0)
label3.grid(column=3, row=10)


# PLACE

# label1.place(x=10, y=10)
# label2.place(x=50, y=100)
# label3.place(x=300, y=300)






window.mainloop()