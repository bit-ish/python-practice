from tkinter import *
import math

from numpy.ma.extras import row_stack

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    check_label.config(text="")
    title_label.config(text="TIMER")
    canvas.itemconfig(timer_text,text="00:00")

    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 ==0 :
        count_down(long_break_sec)
        title_label.config(text="LONG BREAK" ,font=(FONT_NAME,30,"bold"),fg=RED,bg=GREEN
                           )
    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_label.config(text="SHORT BREAK" ,font=(FONT_NAME,30,"bold"),fg=PINK,bg=GREEN)
    else:
        count_down(work_sec)
        title_label.config(text="WORK UP!" ,font=(FONT_NAME,30,"bold"),fg="black",bg=GREEN)
    print(reps)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps,timer
    count_min=math.floor(count / 60)
    count_sec= count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    if count > 0 :
        timer=window.after(1000,count_down,count-1)

    else:
        start_countdown()
        mark=" "
        work_sessions=math.floor(reps/2)

        for a in range(work_sessions):
            mark += "✅"
        check_label.config(text=mark,bg=GREEN)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title( "POMODORO" )
window.minsize( width=500 , height=400)
window.config( pady=50 , padx=50 , bg=GREEN)


tomato_image=PhotoImage( file="tomato.png" )

canvas=Canvas( width=222 , height=240 , bg=GREEN , highlightthickness=0 )
canvas.create_image(110 , 115 , image=tomato_image )
timer_text=canvas.create_text( 110 , 135 , text="00:00" , fill="white" , font=(FONT_NAME,30,"bold") )
canvas.grid(row=1,column=1)


start_button=Button(text="Start",highlightthickness=0,fg="black",font=("Courier",13,"bold"),command=start_countdown)
start_button.grid(row=2,column=0)


reset_button=Button(text="Reset",highlightthickness=0,fg="black",font=("Courier",13,"bold"),command=reset_timer)
reset_button.grid(row=2,column=2)

check_label=Label(text=" ",bg=GREEN)
check_label.grid(row=3,column=1)

title_label=Label(text="TIMER",font=(FONT_NAME,30,"bold"),fg=YELLOW,bg=GREEN)
title_label.grid(row=0,column=1)

window.mainloop()