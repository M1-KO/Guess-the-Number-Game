# Game rules:
#   1. Choose the game mode between: easy, medium, hard, custom,
#   2. If you choose custom, input integer numbers to define range,
#   3. Guess a number between range of numbers in defined limit.

# Winning condition:
#     Guessing the correct number within the given number of guesses.

# Import necessary library
import random

# Welcome message
print(".:Welcome to Guess the Number Game:.")


# Function to start the game
def start_game():
    while True:
        # Prompt for difficulty level
        print('Select difficulty level: Easy, Medium, Hard, Custom: ')
        difficulty = str(input().casefold())

        # Check if difficulty level is valid and start game mode accordingly
        if difficulty in ['easy', 'medium', 'hard', 'custom']:
            game_mode(difficulty)
            break
        else:
            print("Invalid answer.")


# Function to start game mode based on difficulty level
def game_mode(difficulty):
    # Set game parameters based on difficulty level
    if difficulty == 'easy':
        random_number = random.randint(1, 10)
        limit = 4
        min_value = 1
        max_value = 10
    elif difficulty == 'medium':
        random_number = random.randint(1, 100)
        limit = 7
        min_value = 1
        max_value = 100
    elif difficulty == 'hard':
        random_number = random.randint(-500, 500)
        limit = 10
        min_value = -500
        max_value = 500
    elif difficulty == 'custom':

        # Create empty list for values form player
        custom_values = []

        # Ask for custom range and set game parameters accordingly
        while True:
            x = input("Input integer range from: ")
            try:
                x = int(x)
                custom_values.append(x)
                break
            except ValueError:
                print("Invalid answer.")

        while True:
            y = input("Input integer range to: ")
            try:
                y = int(y)
                custom_values.append(y)
                break
            except ValueError:
                print("Invalid answer.")

        # Add and sort values to the empty list form the lowest to the highest
        custom_values.sort()
        min_value = custom_values[0]
        max_value = custom_values[1]

        # Check if custom range is valid
        if x == y:
            print("Nice try, but that would be too easy \U0001F609")
            game_mode(difficulty)
        else:
            random_number = random.randint(min_value, max_value)

        abs_sub_x_y = abs(x - y)

        # Set up the limit
        if abs_sub_x_y == 1:
            limit = 1

        else:
            for limit in range(0, abs_sub_x_y + 1):
                if 2 ** limit >= abs_sub_x_y:
                    break

    # Start the game with the selected parameters
    game(difficulty, random_number, limit, min_value, max_value)


# Function to play the game
def game(difficulty, random_number, limit, min_value, max_value):
    # Display game parameters
    print(f".:{difficulty.upper()} MODE:.")
    print(f"Guess a number between {min_value} and {max_value}. You have {limit} guesses.")

    # Set attempts counter to 0
    attempts = 0

    # Set beginning sort_min, sort_max values, edge_min, edge_max
    sort_min = min_value
    sort_max = max_value
    edge_min = min_value
    edge_max = max_value

    # Loop until the player guesses the number or runs out of attempts
    while True:
        try:
            # Set countdown
            countdown = limit
            while countdown >= 0:

                # End game if player is out of guesses
                if countdown == 0:
                    print(f"Sorry, you didn't guess the number. It was {random_number}.")
                    break

                # Calculate win probability for next guess
                if countdown == limit:
                    win_probability = (1 / (abs(sort_min - sort_max) + 1) * 100)
                    print(f"Probability of winning in next guess: {round(win_probability, 2)}%")
                elif (sort_min == min_value) ^ (sort_max == max_value):
                    win_probability = 1 / (abs(sort_min - sort_max)) * 100
                    print(f"Probability of winning in next guess: {round(win_probability, 2)}%")
                else:
                    win_probability = 1 / (abs(sort_min - sort_max) - 1) * 100
                    print(f"Probability of winning in next guess: {round(win_probability, 2)}%")

                # Reset loop if player guess is not in range of numbers
                guess = int(input(f"You have {countdown} guesses left: "))
                # if guess not in range(sort_min, sort_max + 1):
                #     print(f"Please enter a valid number between {sort_min} and {sort_max}.")
                #     continue

                # Show information about the guess
                if guess == random_number:
                    if guess == (countdown == limit):
                        print(f"Nice!, the number was {random_number} and You guessed it in your 1st attempt!")
                        break
                    else:
                        attempts += 1
                        print(f"Nice!, the number was {random_number} and You guessed it in {attempts} attempts!")
                        break

                elif guess < random_number:
                    if guess == edge_min:
                        print("Too low!")
                        edge_min += 1
                        sort_min = guess
                    elif guess <= sort_min:
                        print("Invalid answer.")
                        continue
                    elif guess < sort_max:
                        print("Too low!")
                        sort_min = guess

                else:
                    if guess == edge_max:
                        print("Too high!")
                        edge_max -= 1
                        sort_max = guess
                    elif guess >= sort_max:
                        print("Invalid answer.")
                        continue
                    elif guess > sort_min:
                        print("Too high!")
                        sort_max = guess

                # Add attempt counter
                attempts += 1

                # -1 to countdown
                countdown -= 1

        except ValueError:
            print("Invalid answer.")

        else:
            break

    # Function to start new or exit game
    def new_quit_game():

        print("Do you want to play again? Yes/No ")
        answer = str(input()).casefold()

        if answer == "yes":
            start_game()
        elif answer == "no":
            print("Thanks for playing and see You soon!")
        else:
            print("Invalid answer.")
            new_quit_game()

    new_quit_game()


# Program calls the "start_game()" function, which initiates the game
if __name__ == "__main__":
    start_game()
