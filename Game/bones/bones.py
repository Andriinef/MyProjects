import random
import time
from tkinter import *


def bros():
    x = random.choice(["image/b.png", "image/b2.png",
                       "image/b3.png", "image/b4.png",
                       "image/b5.png", "image/b6.png"])  # Рандомный выбор
    return x


def img():
    global b1, b2
    for i in range(18):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1["image"] = b1
        lab2["image"] = b2
        root.update()
        time.sleep(0.12)


"""Создаем экран"""
root = Tk()
root.geometry("400x200")
root.title("Игра в кости. Сделай бросок.")
root.resizable(height=False, width=False)  # Изменяемый размер
root.iconphoto(True, PhotoImage(file="image/iconka.png"))
font = PhotoImage(file="image/holst.png")
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind("<1>", img)
img()

root.mainloop()
