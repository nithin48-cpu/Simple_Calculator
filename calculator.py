from tkinter import *

window = Tk()

window.title("Calculator")
window.geometry("400x400")

e = Entry(window, width=50, borderwidth=5)
e.place(x=0, y=0)


def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))


def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)


def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)


def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)


def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)


def equal():
    n2 = e.get()
    e.delete(0, END)
    global j
    j = int(n2)
    if math == "addition":
        result = i + j
        e.insert(0, str(result))
    elif math == "subtraction":
        result = i - j
        e.insert(0, str(result))
    elif math == "multiplication":
        result = i * j
        e.insert(0, str(result))
    else:
        result = i // j
        e.insert(0, str(result))


def clear():
    e.delete(0, END)


b = Button(window, text='1', width=12, command=lambda: click(1))
b.place(x=10, y=60)

b = Button(window, text='2', width=12, command=lambda: click(2))
b.place(x=80, y=60)

b = Button(window, text='3', width=12, command=lambda: click(3))
b.place(x=170, y=60)

b = Button(window, text='4', width=12, command=lambda: click(4))
b.place(x=10, y=120)

b = Button(window, text='5', width=12, command=lambda: click(5))
b.place(x=80, y=120)

b = Button(window, text='6', width=12, command=lambda: click(6))
b.place(x=170, y=120)

b = Button(window, text='7', width=12, command=lambda: click(7))
b.place(x=10, y=180)

b = Button(window, text='8', width=12, command=lambda: click(8))
b.place(x=80, y=180)

b = Button(window, text='9', width=12, command=lambda: click(9))
b.place(x=170, y=180)

b = Button(window, text='0', width=12, command=lambda: click(0))
b.place(x=10, y=240)

b = Button(window, text='+', width=12, command=lambda: add())
b.place(x=80, y=240)

b = Button(window, text='-', width=12, command=lambda: sub())
b.place(x=170, y=240)

b = Button(window, text='*', width=12, command=lambda: mult())
b.place(x=10, y=300)

b = Button(window, text='/', width=12, command=lambda: div())
b.place(x=80, y=300)

b = Button(window, text='=', width=12, command=lambda: equal())
b.place(x=170, y=300)

b = Button(window, text='clear', width=12, command=lambda: clear())
b.place(x=10, y=350)

window.mainloop()
