import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_guesses = 0
data = pandas.read_csv("50_states.csv")
guessed_states = []



all_states = data.state.to_list()


while correct_guesses < 50:

    answer_state = screen.textinput(title=f"Guess the state. {correct_guesses}/50", prompt="What's another state's name?").title()

    #Check if the user's guess is correct and they haven't guessed it before
    if answer_state in data["state"].values and answer_state not in guessed_states:
        correct_guesses += 1 #Add to correct guesses
        guessed_states.append(answer_state) #Add to guessed_states list
        #Create a Turtle, PenUP, Hide
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()

        #Get the new x and y
        row = data[data["state"] == answer_state]
        new_x = row.x.item() #int(row["x"])
        new_y = row.y.item() #int(row["y"])

        #Go to coor and write
        new_turtle.goto(new_x, new_y)
        new_turtle.write(arg = answer_state)

    if answer_state == "Exit":
        # missed_states = []
        #
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        #
        missed_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break



#States to learn.csv

screen.exitonclick()