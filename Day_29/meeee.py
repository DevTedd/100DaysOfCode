from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#Lets start by creating the text file
#--------------------------------------------------------Global
GREEN = "#f7f5dd"
FONT_NAME = 'Georgia'
#--------------------------------------------------------Password Generator

#Password Generator Project

def gen_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols)for item in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers)for item in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0,password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Alert!!", message='The generated password is copied into your clipboard')
        


#--------------------------------------------------------Save password
#Then we get the inputs from the entrry boxes
def collect_entries():
    web = website_entry.get()
    em = email_entry.get()
    paz = password_entry.get()
    new_entry = f"{web}  |  {em}  |  {paz} \n"
    print(new_entry)
    
    #Input Validation
    if len(web) == 0 or len(paz) == 0:
        messagebox.showinfo(title="OOps", message='Please dont leave any fields empty')
        
    else: 
    
        #Confiming entered details
        is_ok = messagebox.askokcancel(title=web, message=f"These are the entered details: \nEmail: {em}  \n Password: {paz} \n Are the details accurate? ")
        if is_ok:
            f = open("data.txt","a")
            f.write(new_entry)
            f.close()
            website_entry.delete(0,END)
            password_entry.delete(0,END)
        
    #Teach version
    # if is_ok: 
    #  with open('data.txt', 'a') as data_file:
    #     data_file.write(f"{web}  |  {em}  |  {paz}\n")
    #     website_entry.delete(0,END)
    #     password_entry.delete(0,END)

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
canvas.grid(column=1,row=0)

#User Input section 
website_label = Label(text = 'Website',font=(FONT_NAME,15))
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1, columnspan=2)
website_entry.focus()


email_label = Label(text = 'Email/Username',font=(FONT_NAME,15))
email_label.grid(column=0, row=2)

email_entry = Entry(width = 35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,'kimanited73@gmail.com')


password_label = Label(text = 'Password',font=(FONT_NAME,15))
password_label.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1 ,row=3)

gen_password = Button(text='Generate Password!', command=gen_password)
gen_password.grid(column=3,row=3)

add_password = Button(text='Add', width=36, command=collect_entries)
add_password.grid(column=1, row=4, columnspan= 2)



window.mainloop()