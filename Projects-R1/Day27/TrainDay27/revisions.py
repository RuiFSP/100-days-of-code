from tkinter import Tk, Label, Button, Entry, END


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # padding

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="Label")
my_label.grid(column=0, row=0)

# Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Button
button = Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

# Entry
my_input = Entry(width=10)
my_input.insert(END, string="Entry")
print(my_input.get())
my_input.grid(column=3, row=2)

window.mainloop()
