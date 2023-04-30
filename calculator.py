from tkinter import *
color = "green"


def show_calculator(window):
    frame = Frame(window)
    frame.pack()
    # Počáteční Vklad
    label_počáteční_vklad = Label(frame, text="Počáteční vklad", font=(12), bg=color, fg="white")
    label_počáteční_vklad.grid(row=0, column=0, padx=10, pady=10)

    label_počáteční_vklad_kč = Label(frame, text="Kč", font=(12), bg=color, fg="white")
    label_počáteční_vklad_kč.grid(row=0, column=2, padx=10, pady=10)

    počáteční_vklad = Entry(frame, width=10, font=(10), bg="white", fg="black")
    počáteční_vklad.grid(row=0, column=1, padx=10, pady=10)

    # Měsíční vklad
    label_měsíční_úložka = Label(frame, text="Měsíční vklad", font=(12), bg=color, fg="white")
    label_měsíční_úložka.grid(row=1, column=0, padx=10, pady=10)

    měsíční_úložka = Entry(frame, width=10, font=(10), bg="white", fg="black")
    měsíční_úložka.grid(row=1, column=1, padx=10, pady=10)

    měsíční_úložka_kč = Label(frame, text="Kč", font=(12), bg=color, fg="white")
    měsíční_úložka_kč.grid(row=1, column=2, padx=10, pady=10)

    # Roční úrok
    label_roční_úrok = Label(frame, text="Roční úrok", font=(12), bg=color, fg="white")
    label_roční_úrok.grid(row=2, column=0, padx=10, pady=10)

    roční_úrok = Entry(frame, width=10, font=(10), bg="white", fg="black")
    roční_úrok.grid(row=2, column=1, padx=10, pady=10)

    roční_úrok_kč = Label(frame, text="%", font=(12), bg=color, fg="white")
    roční_úrok_kč.grid(row=2, column=2, padx=10, pady=10)

    # Doba spoření
    label_doba_spoření = Label(frame, text="Doba spoření", font=(12), bg=color, fg="white")
    label_doba_spoření.grid(row=3, column=0, padx=10, pady=10)

    doba_spoření = Entry(frame, width=10, font=(10), bg="white", fg="black")
    doba_spoření.grid(row=3, column=1, padx=10, pady=10)

    doba_spoření_kč = Label(frame, text="let", font=(12), bg=color, fg="white")
    doba_spoření_kč.grid(row=3, column=2, padx=10, pady=10)

    # Funkcion
    def matematic_operation():
        result = int(počáteční_vklad.get())
        for _ in range(int(doba_spoření.get()) * 12):
            x = (int(měsíční_úložka.get())) + (result / 100 * int(roční_úrok.get())) / 12
            result += x
        result = round(result)
        return result

    def add_gap():
        new_string = ""
        for index, number in enumerate(reversed(str(matematic_operation()))):
            if index == 0:
                new_string += number
            elif index % 3 == 0:
                new_string += " "
                new_string += number
            else:
                new_string += number
        return new_string

    def reversed_result():
        new_string = ""
        for number in reversed(add_gap()):
            new_string += number
        label_spočítat_button["text"] = new_string
        return label_spočítat_button["text"]

    # Button
    spočítat_button = Button(frame, text="Spočítat", font=("", 18, "bold"), bg="white", fg="black", command=(reversed_result))
    spočítat_button.grid(row=4, column=0, padx=10, pady=10)

    label_spočítat_button = Label(frame, text="", font=("", 22), bg=color, fg="white")
    label_spočítat_button.grid(row=4, column=1, padx=10, pady=10)

    label_spočítat_button_kč = Label(frame, text="Kč", font=("", 22), bg=color, fg="white")
    label_spočítat_button_kč.grid(row=4, column=2, padx=10, pady=10)

    return frame
