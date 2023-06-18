from tkinter import *

window = Tk()


# BAŞLIK
window.title('Tkinter giriş videosu')


# RENK# window.configure(background = 'blue')
# window.configure(bg='#00FFE8')
window.configure(bg='black')


# BOYUT VE BAŞLANGIÇ NOKTASI
# window.geometry('300x300+50+100')


# İCON
window.iconbitmap('favicon.ico')


# SAYDAMLIK
window.attributes('-alpha', 0.8)


# HER ZAMAN EN ÜSTTE KALMA (alt tab yapınca en üstte kalması)
# window.wm_attributes('-topmost', 1)


# BOYU VE ENİNİN DEĞİŞTİRİLEBİLMESİ
window.resizable(height=False, width=False)


# MAXİMUM MİNİMUM BOY EN
window.minsize(200, 200)
# window.maxsize(500, 500)


# FULLSCREEN
window.attributes('-fullscreen', True)
window.bind('<Escape>', lambda event: window.attributes('-fullscreen', False))
window.bind("<F11>", lambda event: window.attributes('-fullscreen', not window.attributes('-fullscreen')))

window.mainloop()

