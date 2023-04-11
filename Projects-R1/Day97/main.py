from tkinter import Frame, Label, RIGHT, LEFT, Text, Tk, END
from PIL import Image, ImageTk
import csv


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

            # Create a new frame at the top of the app
            top_frame = Frame(self.root, bg="#222222")
            top_frame.pack(fill='x')

            # Add a label to display the score
            self.score = 0
            self.score_label = Label(top_frame, text=f"Score: {self.score}", font=("Helvetica", 14), fg="#ffffff",
                                     bg="#222222")
            self.score_label.pack(side=LEFT, padx=10)

            # Add an image to display the logo
            self.logo_image = Image.open("logo.jpeg")
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)
            logo_label = Label(top_frame, image=self.logo_photo, bg="#222222")
            logo_label.pack(side=RIGHT, padx=10)

            # Add a label to display the highest score
            self.highest_score = self.load_highest_score()
            self.highest_score_label = Label(top_frame, text=f"Highest Score: {self.highest_score}",
                                             font=("Helvetica", 14), fg="#ffffff", bg="#222222")
            self.highest_score_label.pack(side=LEFT, padx=10)

            self.textbox = Text(self.root, bg="#e6e6e6", fg="#222222", font=("Helvetica", 16))
            self.textbox.pack(pady=20, padx=20)
            self.textbox.config(pady=20, padx=20)

            self.fade_out_job = None

        except Exception as e:
            print(f"Error: {e}")
            exit()

    def load_highest_score(self):
        try:
            with open('scores.csv', mode='r') as file:
                reader = csv.reader(file)
                scores = [int(row[0]) for row in reader if row]
                if scores:
                    return max(scores)
                else:
                    return 0
        except Exception as e:
            print(f"Error: {e}")
            return 0

    def check_typing(self, event):
        try:
            if self.fade_out_job is not None:
                self.root.after_cancel(self.fade_out_job)

            if event.char.isalnum():
                self.textbox.config(fg="#222222", bg="#e6e6e6")
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
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

                # save the score to csv file if it is higher than the current highest score
                if self.score > self.highest_score:
                    with open('scores.csv', mode='w') as file:
                        writer = csv.writer(file)
                        writer.writerow([self.score])
                    self.highest_score = self.score
                    self.highest_score_label.config(text=f"Highest Score: {self.highest_score}")

                self.score = 0
                self.score_label.config(text=f"Score: {self.score}")

            else:
                self.textbox.config(fg='gray50', bg="#e6e6e6")
                self.root.after(50, self.fade_out)
        except Exception as e:
            print(f"Error: {e}")

    def run(self):
        try:
            self.root.after(3000, self.fade_out)
            self.root.mainloop()

        except Exception as e:
            print(f"Error: {e}")
            exit()


app = TypingApp()
app.run()
