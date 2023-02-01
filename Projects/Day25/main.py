import turtle
import pandas
import pandas as pd
from board_data import BoardData

# setup
screen = turtle.Screen()
screen.title(f"Name the States")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
state_list = data['state'].str.capitalize().to_list()
user_board = BoardData()

# variables
num_of_correct_guess = 0
game_is_on = True

while len(state_list) > 0:

    answer_state = screen.textinput(title=f"{len(user_board.list_correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name ?").capitalize()
    if answer_state == "Exit":
        df = pandas.DataFrame(state_list)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        state_list.remove(answer_state)
        user_board.add_correct_guess(answer_state)

        # look for coordinates in list
        x = int(data[data.state.str.capitalize() == answer_state].x)
        y = int(data[data.state.str.capitalize() == answer_state].y)
        user_board.add_name_to_map(x_coord=x, y_coord=y, user_guess=answer_state)



