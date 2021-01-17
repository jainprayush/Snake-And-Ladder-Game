import random
import sys
MAX_VAL=100
snakes = {
    17: 7,
    54: 34,
    62: 19,
    98: 79
}

ladders = {
    3: 38,
    24: 33,
    42: 93,
    72: 84
}


def welcome_msg():
    msg = """
    ###### Welcome to Snakes & Ladders Game #####
    """
    print(msg)


def player_names():
    player1_name = input("\nEnter the name of player 1: ").strip()
    player2_name = input("\nEnter the name of player 2: ").strip()
    print("\n##### Let us start #####")
    return player1_name, player2_name


def dice_value_roll():
    random_dice_value = random.randint(1, 6)
    print("You got a " + str(random_dice_value))
    return random_dice_value


def got_snake(old_value, current_value, player_name):
    print("\n" + player_name + " that's a snake bite.\nYour final position is " + str(current_value))


def got_ladder(old_value, current_value, player_name):
    print("\n" + player_name + " that's a ladder.\nYour final position is " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value
    if current_value > 100:
        print(" You need " + str(MAX_VAL - old_value) + " to win this game ")
        return old_value
    print("\n" + player_name + " your final position is " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake(current_value, final_value, player_name)
    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder(current_value, final_value, player_name)
    else:
        final_value = current_value
    return final_value


def check_win(player_name, position):
    if 100 == position:
        print(player_name + " won the game\n")
        print("###### Game successfully finished #####")
        sys.exit(1)



def start():
    welcome_msg()
    player1_name, player2_name = player_names()
    player1_current_position = 0
    player2_current_position = 0
    while True:
        print("\n1. Enter roll or\n2. Enter any number between 1 and 20\n3. Quit")
        input_p1 = input("\n" + player1_name + ": ")
        while (not((input_p1.isdigit() and 1 <= int(input_p1) <= 20) or (input_p1.lower() == "roll" or input_p1.lower() == "quit"))):
            input_p1 = input("Enter again: ")
        else:
            if (input_p1 == "roll" or input_p1 == "Roll"):
                dice_value = dice_value_roll()
            elif (input_p1 == "Quit" or input_p1 == "quit"):
                print("\n" + player2_name + " wins!!")
                sys.exit(1)
            else:
                dice_value = int(input_p1)
                print("\nYou got a ", dice_value)

        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)
        check_win(player1_name, player1_current_position)

        print("\n1. Enter roll or\n2. Enter any number between 1 and 20\n3. Quit")
        input_p2 = input("\n" + player2_name + ": ")
        while (not((input_p2.isdigit() and 1 <= int(input_p2) <= 20) or (input_p2.lower() == "roll" or input_p2.lower() == "quit"))):
            input_p2 = input("Enter again: ")
        else:
            if (input_p2 == "roll" or input_p2 == "Roll"):
                dice_value = dice_value_roll()
            elif (input_p2 == "Quit" or input_p2 == "quit"):
                print("\n" + player1_name + " wins!!")
                sys.exit(1)
            else:
                dice_value = int(input_p2)
                print("\nYou got a ", dice_value)


        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)
        check_win(player2_name, player2_current_position)


if __name__ == "__main__":
    start()