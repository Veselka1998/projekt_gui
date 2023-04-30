from tkinter import *
import calculator as c

window = Tk()
window.title("Veselka")
window.minsize(700, 480)
window.resizable(False, False)
color = "#2a6100"

# Frame
frame1 = Frame(window, bg="blue")
frame1.pack(side="top")


# Funkcion
def delete():
   for widgets in frame2.winfo_children():
      widgets.destroy()



def animal():
    delete()
    label_animal = Label(frame2, text="Pes", font=("", 35), fg="black")
    label_animal.grid(row=0, column=0)

def person():
    delete()
    label_person = Label(frame2, text="Elon Musk", font=("", 35), fg="black")
    label_person.grid(row=0, column=0)

def car():
    delete()
    label_car = Label(frame2, text="Mercedes", font=("", 35), fg="black")
    label_car.grid(row=0, column=0)

def calculator():
    delete()
    c.show_calculator(window)
    


label_menu = Label(frame1, text="MENU", font=("", 25, "bold"), bg="blue", fg="white", width=5)
label_menu.grid(row=0, column=0, padx=10, pady=10)

button1 = Button(frame1, text="Náš Fotbal", font=("times new roman", 18, "bold"), bg="white", fg="black", width=10, command=animal)
button1.grid(row=0, column=1, padx=10, pady=10)

button2 = Button(frame1,text="Hry", font=("times new roman", 18, "bold"), bg="white", fg="black", width=10, command=person)
button2.grid(row=0, column=2, padx=10, pady=10)

button3 = Button(frame1,text="Akcie", font=("times new roman", 18, "bold"), bg="white", fg="black", width=10, command=car)
button3.grid(row=0, column=3, padx=10, pady=10)

button4 = Button(frame1, text="Kalkulačka", font=("times new roman", 18, "bold"), bg="white", fg="black", width=10, command=calculator)
button4.grid(row=0, column=4, padx=10, pady=10)


window.mainloop()