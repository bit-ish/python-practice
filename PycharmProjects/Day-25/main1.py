import turtle,pandas

screen=turtle.Screen()
screen.title("U.S. States Name")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
states_data=data["state"]
print(type(states_data))

timmy=turtle.Turtle()
timmy.hideturtle()
timmy.penup()


# game_is_on=True

score=0
states_found=[]

while score<=50:

    user_state_guess=screen.textinput(f"{score}/50 Guess the State","what's your guess?").title()

    if user_state_guess=="Exit":
        break

    for guess in states_data:
        if user_state_guess==guess:
            if guess not in states_found:
                timmy.goto(int(data[states_data==guess].x),int(data[states_data==guess].y))
                timmy.write(f"{guess}",False,"center",("Arial",10,"bold"))
                score+=1
                states_found.append(guess)


# states_to_learn.csv
states_to_learn=[]

for states in states_data:
    if states not in states_found:
        states_to_learn.append(states)


states_to_learn=pandas.DataFrame( states_to_learn).to_csv("states_to_learn.csv")
