import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25*60
SHORT_BREAK_SEC = 5*60
LONG_BREAK_SEC = 10*60
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text='')
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        timer_label.config(text="Break",fg=RED)
        count_down(LONG_BREAK_SEC)
    elif reps%2==0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_SEC)
    elif reps%2==1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_SEC)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=(count%60)
    if count_sec<10:
        count_sec=f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        worked=math.floor(reps/2)
        mark=''
        for i in range(worked):
            mark+='✔'
        check_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_label=Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
timer_label.grid(column=2,row=1)

canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text=canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=2,row=2)

start_button=Button(text='Start',command=start_timer, highlightthickness=0)
start_button.grid(column=1,row=3)

reset_button=Button(text='Reset',command=reset_timer, highlightthickness=0)
reset_button.grid(column=3,row=3)

check_label=Label(fg=GREEN, highlightthickness=0,bg=YELLOW)
check_label.grid(column=2,row=4)


window.mainloop()
