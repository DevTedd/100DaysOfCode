from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#219C90"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
fG = RED
reps = 1# number of repitions 
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)#stopping the loop 
    #change title, checkmarks and time
    title_label.config(text='Timer', fg=RED)
    runs_done.config(text='')
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    
    
    
    
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    
    work_sec = WORK_MIN * 60
    SHORT_BREAK_sec = SHORT_BREAK_MIN * 60
    LONG_BREAK_Sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_Sec)   
        title_label.config(text='Long Break!', fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_sec)
        title_label.config(text='Short Break!', fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text='Work Sesh - Stay Focused', fg=YELLOW)
        
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # if count_sec == 0 or count_min == 0:
    #     count_sec = "00"
    #     count_min = "00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # if reps % 2 == 0:
        #     runs_done.config(text='✓')
        marks = ""
        work_sesh = math.floor(reps/2)
        for x in range(work_sesh):
            marks += '✓'
        runs_done.config(text=marks)
            


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100,pady=50,bg=GREEN)


title_label = Label(text='Timer', fg=fG, bg=GREEN, font=(FONT_NAME,50))
title_label.grid(column=1, row=0)


#Using the canvas option
canvas = Canvas(width=200,height=224, bg=GREEN,highlightthickness=0)
tomato_img = PhotoImage(file='C:/Users/tkmwangi/Documents/GitHub/100DaysOfCode/Day_28/tomato.png')
canvas.create_image(100,112, image = tomato_img )#to place it in the center
timer_text = canvas.create_text(102,130, text='00:00', fill='white', font = (FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)



#Buttons
start_button = Button(text = 'Start Timer', highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
reset_button = Button(text = 'Reset Timer', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

#Checkbox
runs_done = Label(fg=GREEN, bg=RED)
runs_done.grid(column=1, row=3)



window.mainloop()
