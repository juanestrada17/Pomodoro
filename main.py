from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    reset_time()
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    start_time()
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_title.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# LABEL

timer_title = Label(text="Timer", font=("Helvetica", 40, "bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)
# two buttons
start = Button(text="Start", font=("Helvetica", 15, "bold"), command=start_timer, state="normal")
start.grid(column=0, row=2)

reset = Button(text="Reset", font=("Helvetica", 15, "bold"), command=reset_timer, state="disabled")
reset.grid(column=2, row=2)

# check mark label
check_mark = Label(font=("Helvetica", 15, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


# Enable - Disable buttons
def start_time():
    start.config(state="disabled")
    reset.config(state="normal")


def reset_time():
    start.config(state="normal")
    reset.config(state="disabled")
    global reps
    reps = 0


window.mainloop()
