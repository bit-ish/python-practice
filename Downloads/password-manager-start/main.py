from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter=[choice(letters) for n in range(randint(8, 10))]
    password_symbol=[choice(numbers) for nm in range(randint(2, 4))]
    password_number=[choice(symbols) for nq in range(randint(2, 4))]

    password_list = password_number + password_letter + password_symbol
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password= "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website=web_entry.get().title()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)>0 and len(password)>0 :
        is_ok = messagebox.askokcancel(title="Confirmation",
                                       message=f"Do you want to save \nwebsite: {website}\nemail: {email}\npassword:{password}")


        if is_ok:
            with open("data.txt",mode="a") as file:

                #   .get() is used to get value inside entry box
                file.write(f'{website} | {email } | {password}\n')

        #   .delete() is used to delete value inside entry box (0 and END tells from-to
            web_entry.delete(0,END)
            password_entry.delete(0,END)
    else:
        messagebox.showerror(title="missing field",message="oops; you left a field empty.")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.config(padx=50,pady=50,bg="white")
window.title("Password Manager")

canvas=Canvas(width=200,height=200,background="white",highlightthickness=0)
my_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=my_image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:",bg="white",fg="black")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:", bg="white", fg="black")
email_label.grid(row=2,column=0)

password_label=Label(text="Password:",bg="white",fg="black")
password_label.grid(row=3,column=0)

web_entry=Entry(width=40,bg="white",highlightthickness=0,fg="black")
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()

email_entry=Entry(width=40,bg="white",highlightthickness=0, fg="black")
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"ishy@gmail.com")


password_entry=Entry(bg="white",highlightthickness=0,width=23 ,fg="black")
password_entry.grid(row=3,column=1)

gen_pass_button=Button(text="Generate Password",bg="white" ,highlightthickness=0,pady=0,command=gen_pass)
gen_pass_button.grid(row=3,column=2)

add_button=Button(text="Add",bg="white",highlightthickness=0,pady=0,width=37 , command=save_password)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()