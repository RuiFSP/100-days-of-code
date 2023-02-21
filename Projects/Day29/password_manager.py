from tkinter import Tk, Canvas, PhotoImage, Label, Button, Entry, END, messagebox, Scale
from random import choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(int(scale_letters.get()))]
    password_symbols = [choice(symbols) for _ in range(int(scale_symbols.get()))]
    password_numbers = [choice(numbers) for _ in range(int(scale_numbers.get()))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, string=password)

    # password copied to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Invalid inputs", message="Please don't leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website} "
                                                              f"\nEmail: {email} \nPassword: {password} "
                                                              f"\nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as f:
                f.write(f"{website} | {email} | {password}\n")
                clear_fields()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# mypass canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

# --------- Labels
# website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# email label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
# password label
password_label = Label(text="Password")
password_label.grid(column=0, row=3)
# letters label
letters_label = Label(text="How many letters ?")
letters_label.grid(column=0, row=5)
# symbols label
symbols_label = Label(text="How many symbols ?")
symbols_label.grid(column=0, row=6)
# numbers label
numbers_label = Label(text="How many  numbers?")
numbers_label.grid(column=0, row=7)
# --------- Entries
# website entry
website_entry = Entry(width=52)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus()
# email entry
email_entry = Entry(width=52)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "myemail@gmail.com")  # default value
# password entry
password_entry = Entry(width=33)
password_entry.insert(END, string="aDAdaSDS$%SAS.")
password_entry.grid(column=1, row=3)

# --------- Buttons
# generate password button
generate_password_button = Button(text="Generate Password", command=generate_password, bg="white")
generate_password_button.grid(column=2, row=3)
# save password button
save_password_button = Button(text="Save Password", width=44, command=save)
save_password_button.grid(column=1, columnspan=2, row=4)

# ---------- Scales
scale_letters = Scale(from_=3, to=9, orient="horizontal", length=320)
scale_letters.grid(row=5, column=1, columnspan=2)

scale_symbols = Scale(from_=3, to=9, orient="horizontal", length=320)
scale_symbols.grid(row=6, column=1, columnspan=2)

scale_numbers = Scale(from_=3, to=9, orient="horizontal", length=320)
scale_numbers.grid(row=7, column=1, columnspan=2)

window.mainloop()
