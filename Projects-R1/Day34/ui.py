from tkinter import Tk, Label, Canvas, PhotoImage, Button
from quiz_brain import QuizBrain

THEME_COLOR = "#13005A"
TEXT_FONT = ("ariel", 20, "italic")
SCORE_FONT = ("ariel", 15, "bold")


class QuizInterface:

    # input has a quiz_brain object with: quiz_brain: QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.check_answer = None
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz Mania")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}",
                                 bg=THEME_COLOR,
                                 fg="white",
                                 font=SCORE_FONT)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_test = self.canvas.create_text(
            150,
            125,
            width=280,  # the text will adjust to canvas if we provide width
            text="Some question text",
            fill=THEME_COLOR,
            font=TEXT_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_true = PhotoImage(file="images/true.png")

        self.true_button = Button(image=img_true, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        img_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=img_false, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # reset canvas color
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_test, text=q_text)
        else:
            self.canvas.itemconfig(self.question_test, text="You've reached the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
