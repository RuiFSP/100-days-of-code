from tkinter import *

class TypingApp:
    def __init__(self):
        try:
            self.root = Tk()
            self.root.title("Typing App")
            self.root.geometry("600x400")
            self.root.config(bg="#222222")
            self.alpha = 1.0
            self.root.resizable(False, False)
            self.root.bind("<Key>", self.check_typing)

            # Add an image to the app
            self.logo = PhotoImage(file="logo.png")
            self.logo_label = Label(self.root, image=self.logo, bg="#222222")
            self.logo_label.pack()

            # Add a label to the app
            self.score_label = Label(self.root, text="Score: 0", fg="white", bg="#222222", font=("Helvetica", 14))
            self.score_label.pack(pady=10)

            self.textbox = Text(self.root, bg="#e6e6e6", fg="#222222", font=("Helvetica", 16))
            self.textbox.pack(pady=10)

            self.fade_out_job = None
        except Exception as e:
            print(f"Error: {e}")
            exit()

    def check_typing(self, event):
        try:
            if self.fade_out_job is not None:
                self.root.after_cancel(self.fade_out_job)

            if event.char.isalnum():
                self.textbox.config(fg="#222222", bg="#e6e6e6")
            else:
                self.textbox.config(fg="#aaaaaa", bg="#e6e6e6")

            self.fade_out_job = self.root.after(3000, self.fade_out)
        except Exception as e:
            print(f"Error: {e}")

    def fade_out(self):
        try:
            self.alpha -= 0.05
            if self.alpha <= 0:
                self.alpha = 0
                self.textbox.delete("1.0", END)
                self.textbox.config(fg="black", bg="white")
            else:
                self.textbox.config(fg='gray50', bg="#e6e6e6")
                self.root.after(50, self.fade_out)
        except Exception as e:
            print(f"Error: {e}")

    def run(self):
        try:
            self.root.mainloop()
        except Exception as e:
            print(f"Error: {e}")
            exit()

app = TypingApp()
app.run()
