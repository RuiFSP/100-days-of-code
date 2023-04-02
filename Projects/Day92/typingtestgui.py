import time
import tkinter as tk
import csv


class TypingTestGUI(tk.Frame):
    """
    A GUI application that tests your typing speed.
    """

    def __init__(self, master: tk, test_string: str) -> None:
        """
        Creates a new TypingTestGUI instance.

        Parameters
        ----------
        master : tk.Tk
            The root window of the application.
        test_string : str
            The text that the user needs to type.
        """
        super().__init__(master)
        self.master = master
        self.master.title("Typing Test")
        self.master.geometry("600x400")
        self.master.resizable(False, False)
        self.master.configure(bg="#F6F6F6")
        self.test_string = test_string
        self.time_start = None
        self.best_wpm = 0
        with open('best_wpm.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            try:
                row = next(reader)
                self.best_wpm = int(row[0])
            except (StopIteration, ValueError):
                pass

        # Set the font for the labels and the entry field
        font = ("Arial", 14)

        # Create label widgets
        self.best_wpm_label = tk.Label(
            self.master, text=f"Best WPM: {self.best_wpm}", bg="#F6F6F6", font=("Helvetica", 12)
        )
        self.best_wpm_label.pack(side=tk.TOP, pady=10)
        self.instruction_label = tk.Label(self, text="Type the following text:", font=font, bg="#F6F6F6")
        self.text_label = tk.Label(self, text=self.test_string, font=font, bg="#F6F6F6", wraplength=500,
                                   justify=tk.CENTER, bd=5, relief=tk.SOLID)

        # Create entry widget
        self.input_entry = tk.Entry(self, font=font, bd=5, relief=tk.SOLID)

        # Create start button widget
        self.start_button = tk.Button(self, text="Start", font=font, bg="#4CAF50", fg="white", bd=5, relief=tk.SOLID,
                                      command=self.start_test)

        # Pack widgets
        self.instruction_label.pack(pady=10)
        self.text_label.pack(pady=20)
        self.input_entry.pack(pady=10)
        self.start_button.pack(pady=10)

        self.pack()

    def start_test(self) -> None:
        """
        Starts the typing test and disables the "Start" button.
        """
        if not isinstance(self.input_entry, tk.Entry):
            raise TypeError("self.entry_input must be of type tkinter.Entry")
        if not isinstance(self.start_button, tk.Button):
            raise TypeError("self.button_start must be of type tkinter.Button")
        if not isinstance(self.time_start, float) and self.time_start is not None:
            raise TypeError("self.time_start must be a float or None")

        # Clear the input field and set focus to it
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()

        # Disable the "Start" button to prevent the user from starting the test again
        self.start_button.config(state=tk.DISABLED)

        # Record the start time of the test
        self.time_start = time.time()

        # Bind the "Return" key to the "end_test" method, so that the test ends when the user presses "Enter"
        self.input_entry.bind("<Return>", self.end_test)

    def end_test(self, event=None, arg2=None) -> None:
        """
        Ends the typing test, calculates the typing speed, and displays it.
        """
        # Calculate the elapsed time
        time_end = time.time()
        elapsed_time = time_end - self.time_start

        # Get the user's input text and calculate the typing speed
        input_text = self.input_entry.get()
        wpm = self.calculate_wpm(input_text, elapsed_time)

        # Update the instruction label to display the typing speed
        self.instruction_label.config(text=f"Your typing speed is {wpm} WPM!")

        # if the current WPM is better than the previous best WPM, update the CSV file
        if wpm > self.best_wpm:
            self.best_wpm = wpm
            self.save_best_wpm()

        # Enable the start button and unbind the "Return" key
        self.start_button.config(state=tk.NORMAL)
        self.input_entry.unbind("<Return>")

    def calculate_wpm(self, input_text: str, elapsed_time: float) -> int:
        """
        Calculates the typing speed in words per minute.

        Parameters
        ----------
        input_text : str
            The text that the user typed.
        elapsed_time : float
            The time elapsed during the typing test.

        Returns
        -------
        int
            The typing speed in words per minute.
        """
        input_words = input_text.strip().split()
        test_words = self.test_string.strip().split()
        correct_word_count = 0
        for i, word in enumerate(input_words):
            if i >= len(test_words):
                break
            if word == test_words[i]:
                correct_word_count += 1
        wpm = int(correct_word_count / elapsed_time * 60)
        return wpm

    def save_best_wpm(self) -> None:
        """
        Saves the current best WPM to a CSV file.
        """
        with open('best_wpm.csv', mode='w', newline='') as file:
            # Create the CSV writer
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(['Best WPM'])

            # Write the best WPM value
            writer.writerow([self.best_wpm])
