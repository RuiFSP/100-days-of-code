from tkinter import Entry, Label, Button, Tk

MY_FONT = ("arial", 12, "bold")
CONST_TO_CONVERT = 1.609

# Creating window and configuration
window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=50, pady=50)


def calculate():
    conversion = float(user_entry.get()) * CONST_TO_CONVERT
    label_output.config(text=conversion)


# Entry Miles
user_entry = Entry(width=10, font=MY_FONT)
user_entry.grid(column=1, row=0)

# Label miles
label_miles = Label(text="Miles", font=MY_FONT)
label_miles.grid(column=2, row=0)

# Label is equal
label_equal = Label(text="is equal to", font=MY_FONT)
label_equal.grid(column=0, row=1)

# Label output
label_output = Label(text="0", font=MY_FONT)
label_output.grid(column=1, row=1)

# Label km
label_km = Label(text="Km", font=MY_FONT)
label_km.grid(column=2, row=1)

# Button
button = Button(text="Calculate", font=MY_FONT, command=calculate)
button.grid(column=1, row=2)

window.mainloop()
