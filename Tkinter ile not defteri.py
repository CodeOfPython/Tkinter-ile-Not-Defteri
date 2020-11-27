from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

pncr = tk.Tk()
pncr.title('Not Defteri')


def çıkış():
    global pncr
    pncr.quit()


def get_textarea_value():
    global textarea
    return textarea.get("1.0", END)


def kaydet():
    global pncr
    data = get_textarea_value()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt",
                                 filetypes=(("Yazı dosyası", "*.txt"), ("Tüm Dosyalar", "*.*")), title='Kaydet',
                                 initialdir=pncr.winfo_pathname)
    if f != None:
        f.write(data)
        f.close()


def aç():
    global textarea
    f = filedialog.askopenfile(mode='r', defaultextension=".txt",
                               filetypes=(('Yazı Dosyası', '*.txt'), ('Tüm Dosyalar', '*.*')), title='Aç',
                               initialdir=pncr.winfo_pathname)
    if f == None:
        return
    text = f.read()
    if text != None:
        textarea.delete(1.0, END)
        textarea.insert(END, text)


def yeni():
    global textarea
    textarea.delete(1.0, END)


def hakkında():
    messagebox.showinfo('Hakkında',
                        'Bu program yazı yazmak, okumak, yazıyı düzenlemek için yazılmıştır')


menubar = Menu(pncr)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Yeni', command=yeni)
filemenu.add_command(label='Aç', command=aç)
filemenu.add_command(label='Kaydet', command=kaydet)
filemenu.add_separator()
filemenu.add_command(label='Çıkış', command=çıkış)
menubar.add_cascade(label='Dosya', menu=filemenu)
menubar.add_command(label='Hakkında', command=hakkında)

textarea = Text(pncr, width=100, height=20)
textarea.pack()

pncr.configure(background='white')
pncr.config(menu=menubar)
pncr.mainloop()

















