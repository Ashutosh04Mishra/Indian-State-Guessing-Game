import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("Indian States Guessing Game")
image = "India.gif"
screen.addshape(image)
t.shape(image)
tim = t.Turtle()

data = pd.read_csv("Indian_States.csv")
states_list = data.States.to_list()
guessed_state = []

while len(guessed_state) < 33 :
    answer_state = screen.textinput(title=f"{len(guessed_state)}/33 correct",prompt="Enter a state name :").title()
    if answer_state == "Exit" :
        missed_state = []
        for state in states_list:
            if state not in guessed_state:
                missed_state.append(state)
        data_frame = pd.DataFrame(missed_state)
        data_frame.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list :
        guessed_state.append(answer_state)
        tim.hideturtle()
        tim.penup()
        state_data = data[data.States == answer_state]
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(answer_state)




















