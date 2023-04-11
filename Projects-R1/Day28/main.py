from tkinter import Tk, Canvas, PhotoImage, Label, Button
from playsound import playsound
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFB26B"
RED = "#FF7B54"
GREEN = "#FFD56F"
YELLOW = "#939B62"

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- PLAY SOUND -------------------------------- #
def play():
    playsound('alarm.wav')


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label_timer.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_timer.config(text="RELAX", fg=PINK)
    else:
        countdown(work_sec)
        label_timer.config(text="FOCUS", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        working_sessions = math.floor(reps / 2)
        for _ in range(working_sessions):
            marks += "✔"

        label_check_mark.config(text=marks)
        play()  # alarm


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# label timer
label_timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

# tomato canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# button start
start_button = Button(text="Start", highlightthickness=0, command=start_timer, font=(FONT_NAME, 15, "bold"), bg=GREEN)
start_button.grid(column=0, row=2)

# button end
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, font=(FONT_NAME, 15, "bold"), bg=GREEN)
reset_button.grid(column=2, row=2)

# label check maker
label_check_mark = Label(fg=GREEN, bg=YELLOW)
label_check_mark.grid(column=1, row=3)

window.mainloop()
