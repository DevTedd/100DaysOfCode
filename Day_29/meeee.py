from tkinter import *


#--------------------------------------------------------Global
GREEN = "#f7f5dd"
FONT_NAME = 'Georgia'
#--------------------------------------------------------Password Generator

#--------------------------------------------------------Save password

#--------------------------------------------------------UI
window = Tk()
window.title('Offline Password Manager')
window.config(padx=20,pady=20,bg=GREEN,)

# title_label = Label(text="Ted's Password Manager",font=("Courier",50))
# title_label.grid(column=1, row=0)

#Logo section 
canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file='C:/Users/tkmwangi/Documents/GitHub/100DaysOfCode/Day_29/logo.png')
canvas.create_image(100,100, image = lock_img )#to place it in the center
canvas.grid(column=1,row=1)

#User Input section 
website_label = Label(text = 'Website',font=(FONT_NAME,15))
website_label.grid(column=0, row=2)

website_entry = Entry()
website_entry.grid(column=0,row=2, columnspan=2)


email_label = Label(text = 'Email/Username',font=(FONT_NAME,15))
email_label.grid(column=0, row=3)

email_entry = Entry()
email_entry.grid(column=0,row=4,columnspan=2)


password_label = Label(text = 'Password',font=(FONT_NAME,15))
password_label.grid(column=0, row=5)

password_entry = Entry()
password_entry.grid(column=1,row=5)

gen_password = Button(text='Generate Password!')
gen_password.grid(column=2,row=5)

add_password = Button(text='Add')
add_password.grid(column=1, row=6, columnspan= 2)



window.mainloop()