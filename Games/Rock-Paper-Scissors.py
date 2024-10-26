import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Make a choice — ({choices_str}): "))
    action = Action(selection)
    return action


def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


def determine_winner(user_act, computer_act):
    if user_act == computer_act:
        print(f"Both users have chosen {user_act.name}. Tie!")
    elif user_act == Action.Rock:
        if computer_act == Action.Scissors:
            print("Rock beats scissors! You win!")
        else:
            print("Paper over rock! You lose.")
    elif user_act == Action.Paper:
        if computer_act == Action.Rock:
            print("Paper over rock! You win!")
        else:
            print("The scissors are cutting paper! You lose.")
    elif user_act == Action.Scissors:
        if computer_act == Action.Paper:
            print("Scissors cut paper! You win!")
        else:
            print("Rock beats scissors! You lose.")


while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Incorrect input. Enter a value from the range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Shall we play again? (yes/no):")
    if play_again.lower() != "yes":
        break
