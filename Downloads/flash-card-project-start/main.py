from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
chosen_dict= { }
to_learn={ }

# reading the data inside a CSV using pandas
try:
    data=pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data= pd.read_csv("data/french_words.csv")
    to_learn= original_data.to_dict(orient="records")


# print(type(data))
else:
# converting data (DataFrame) into a list of dictionaries
 to_learn=data.to_dict(orient="records")

# print(to_learn)

window =Tk()
window.title("Flashy")

window.config(padx=50,pady=50, background=BACKGROUND_COLOR)


flip_timer= None

def next_card():
    global chosen_dict, flip_timer
    # this is done to avoid 3 s timer flip timer running in the background

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    chosen_dict= random.choice(to_learn)
    random_fr_word=  chosen_dict["French"]

    # this changes the property of existing item in canvas
    canvas.itemconfig(card_wfront, image= card_front)
    canvas.itemconfig(card_text, text=f'{random_fr_word}', fill="black")
    canvas.itemconfig(card_title, text= "French", fill="black")
    flip_timer= window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_wfront, image= card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    random_en_word=chosen_dict["English"]
    canvas.itemconfig(card_text, text=f"{random_en_word}", fill="white")

def is_known():
    to_learn.remove( chosen_dict )
    print(len(to_learn))

    # .DataFrame() is the constructor used to create the DataFrame object, which is essentially a two-dimensional table
    # with rows and columns, much like a spreadsheet.
    learning_data=pd.DataFrame(to_learn)
    learning_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
right_image=PhotoImage(file="images/right.png")
wrong_image=PhotoImage(file="images/wrong.png")

canvas=Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
card_wfront= canvas.create_image(400,263, image=card_front)
# the following commands creates as well as assigns the value to a variable
card_title= canvas.create_text(400,150, text="Title",font=("Ariel",40,"italic"), fill="black")
card_text= canvas.create_text(400,260, text="Word",font=("Ariel",60,"bold"), fill="black")

canvas.grid(row=0, column=0, columnspan=2)

wrong_button=Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1,column=0)

check_button= Button(image=right_image, highlightthickness=0, command=is_known)
check_button.grid(row=1,column=1)

next_card()

flip_timer= window.after(3000,flip_card)

window.mainloop()