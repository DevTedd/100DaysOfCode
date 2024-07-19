#imports
from tkinter import *
import pandas as pd
import random

#Static variables
BACKGROUND_COLOR = "#B1DDC6"

swahili = pd.read_csv('flash-card-project-start/data/Swahili to English - Sheet1.csv')
to_learn = swahili.to_dict(orient="records")
current_card = {}

#Functions

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canva.itemconfig(card_title, text = 'Swahili')
    canva.itemconfig(card_word,text=current_card["Swahili"], fill='black')
    canva.itemconfig(card_bg, image =card_front_img)
    flip_timer = window.after(5000,func=flip_card)
    
def flip_card():
    canva.itemconfig(card_title, text ='English')
    canva.itemconfig(card_word,text=current_card['English'])
    canva.itemconfig(card_bg, image='card_back_img')
    
def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pd.df(to_learn)
    data.to_csv('data/words_to_learn')
    next_card()


#UI
window = Tk()
window.title("Flash Cards!")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

#Flipping the card
flip_timer = window.after(5000, func=flip_card)

canva = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='flash-card-project-start/images/card_front.png')
card_back_img = PhotoImage(file='flash-card-project-start/images/card_back.png')
card_bg = canva.create_image(400,263,image=card_front_img)
card_title = canva.create_text(400,150, font=('Arial', 40, "italic"))
card_word = canva.create_text(400,263,font=('Arial', 60, "bold"))
canva.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva.grid(row=0,column=0, columnspan=2)


cross_image = PhotoImage(file='flash-card-project-start/images/wrong.png')
unknow_button = Button(image=cross_image,highlightthickness=0, command=next_card)
unknow_button.grid(row=1,column=0)


check_image = PhotoImage(file='flash-card-project-start/images/right.png')
know_button = Button(image=check_image,highlightthickness=0, command=next_card)
know_button.grid(row=1,column=1)


next_card()

window.mainloop()