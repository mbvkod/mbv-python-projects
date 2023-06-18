from tkinter import *
window = Tk()
window. geometry('400x400')


# Button(window, text='Click me!', font='Times 15 bold', bg='pink', fg='red',
#        activebackground='orange', activeforeground='blue',
#        ).pack()





# cursorlist = [
# "arrow",
# "circle",
# "clock",
# "cross",
# "dotbox",
# "exchange",
# "fleur",
# "heart",
# "heart",
# "man",
# "mouse",
# "pirate",
# "plus",
# "shuttle",
# "sizing",
# "spider",
# "spraycan",
# "star",
# "target",
# "tcross",
# "trek",
# "watch",
# ]
#
# x = 1
# for cursoritem in cursorlist:
#     Button(window, text='Click me! {}'.format(x), cursor=cursoritem).pack(pady=2)
#     x = x + 1




# Button(window, text='Click me!Click meClick meClick me', height= 10, width=20, wraplength=30).pack()




# def clicked_button():
    # Label(window, bg='black', width=40, height=2, text='I will spawn when you click that button', fg='red').pack()
    # print('you clicked me')

# Button(window, text='Click me!', height=10, width=20, bd=10, command=clicked_button).pack()




# Button(window, text='Click me!').pack()
# Button(window, text='Click me!', padx=20).pack()
# Button(window, text='Click me!',pady=20).pack()



# relieflist = [
#     FLAT,
#     RAISED,
#     SUNKEN,
#     GROOVE,
#     RIDGE
# ]
# for reliefitem in relieflist:
#     Button(window, text='{}'.format(reliefitem), relief=reliefitem,).pack(pady=3)




Button(window, text='Click me!').pack(pady=5)
Button(window, text='Click me!', state='normal').pack(pady=5)
Button(window, text='Click me!', state='disabled').pack(pady=5)








window.mainloop()

