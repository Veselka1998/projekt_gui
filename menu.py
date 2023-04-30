from tkinter import *


def show(window):
    frame = Frame(window)

    label_menu = Label(frame, text="MENU", font=("", 25, "bold"), bg="blue", fg="white", width=5)
    label_menu.grid(row=0, column=0, padx=10, pady=10)

    button1 = Button(frame, text="Náš Fotbal", font=("times new roman", 18, "bold"), bg="white", fg="black", width=10, command=animal)
    button1.grid(row=0, column=1, padx=10, pady=10)

    button2 = Button(frame,text="Hry", font=("times new roman", 18, "bold"), bg="white", fg="black", width=10, command=person)
    button2.grid(row=0, column=2, padx=10, pady=10)

    button3 = Button(frame,text="Akcie", font=("times new roman", 18, "bold"), bg="white", fg="black", width=10, command=car)
    button3.grid(row=0, column=3, padx=10, pady=10)

    button4 = Button(frame, text="Kalkulačka", font=("times new roman", 18, "bold"), bg="white", fg="black", width=10, command=calculator)
    button4.grid(row=0, column=4, padx=10, pady=10)
