from tkinter import *
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
def time_reset():
    """Resets the Timer to default state ."""
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="Timer", fg=GREEN)
    reps = 0
    label_2.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Start the timer with a 25 minute work time , as of this program when start putton is clicked."""

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        label_1.config(fg=GREEN)
        label_1["text"] = "Work"
        # work
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        label_1["fg"] = "PINK"
        label_1["text"] = "Break"
        if reps == 2:
            label_2.config(text="✔")
        elif reps == 4:
            label_2.config(text="✔✔")
        elif reps == 6:
            label_2.config(text="✔✔✔")
            # break

    elif reps == 8:
        # break
        count_down(long_break_sec)
        label_1["fg"] = "RED"
        label_1["text"] = "Long Break"
        label_2.config(text="✔✔✔✔")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Starts the count down in as min : sec format when count input isgiven in seconds ."""

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count_min == 0 and count_sec == "00":
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label_1 = Label(
    text="Timer",
    font=(FONT_NAME, 40, "bold"),
    fg=GREEN,
    bg=YELLOW,
    highlightthickness=0,
)
label_1.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./PomodoroApp/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold")
)
canvas.grid(row=1, column=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=time_reset)
reset_button.grid(row=2, column=2)

label_2 = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)
label_2.grid(row=3, column=1)

window.mainloop()
