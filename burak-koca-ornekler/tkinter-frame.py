from tkinter import *
window = Tk()
window.geometry('400x400')

# height
# width
# bg
# highlightbackground
# highlightthickness
# cursor
# padx
# pady



frame1 = Frame(window, height=100, width=200, bg='black',
               highlightbackground='purple', highlightthickness=6,
               cursor='heart',
               padx=20, pady=10)

lbl1 = Label(frame1, text='text1')
lbl1.place(x=0, y=0)


frame1.pack()

window.mainloop()

# CURSOR
# "arrow"
# "circle"
# "clock"
# "cross"
# "dotbox"
# "exchange"
# "fleur"
# "heart"
# "heart"
# "man"
# "mouse"
# "pirate"
# "plus"
# "shuttle"
# "sizing"
# "spider"
# "spraycan"
# "star"
# "target"
# "tcross"
# "trek"
# "watch"
