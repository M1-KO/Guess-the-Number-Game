# # Game rules:
# # A range of numbers that the player can guess from:
# #     Easy - 1 to 10
# #     Medium - 1 to 100
# #     Hard - -500 to 500
#
# # How many guesses the player will get before the game is over:
# # 2tothepower which is bigger than a amount of numbers e.g. range1to100 - guess number = 2 ** x > 100, so here its 7
#
# # Winning condition:
# #     guessing the correct number within the given number of guesses

import random

print(abs(5 - -2))
# x = int(input("Input integer range from: "))
# y = int(input("Input integer range to: "))
#
# x_and_y = abs(x - y)
# print(x_and_y)
#
# if x_and_y == 1:
#     z = 1
#
# elif x or y <= 0:
#     for z in range(0, x_and_y + 1):
#         if 2 ** z >= x_and_y:
#             break
#
# elif x >= y:
#     for z in range(y, x_and_y + 1):
#         if 2 ** z >= x_and_y:
#             break
#
# elif x < y:
#     for z in range(x, x_and_y + 1):
#         if 2 ** z >= x_and_y:
#             break
#
# print(z)



print(".:Welcome to Guess the Number Game:.")


def guess_the_number_game(difficulty):
    if difficulty == 'easy':
        random_number = random.randint(1, 10)
        range_of_numbers = "1 and 10"
        limit = 4
    elif difficulty == 'medium':
        random_number = random.randint(1, 100)
        range_of_numbers = "1 and 100"
        limit = 7
    elif difficulty == 'hard':
        random_number = random.randint(-500, 500)
        range_of_numbers = "-500 and 500"
        limit = 10
    elif difficulty == 'custom':

        while True:
            x = input("Input integer range from: ")
            try:
                x = int(x)
                break
            except ValueError:
                print("Invalid answer.")

        while True:
            y = input("Input integer range to: ")
            try:
                y = int(y)
                break
            except ValueError:
                print("Invalid answer.")

        if x == y:
            print("Nice try, but that would be too easy \U0001F609")
            guess_the_number_game(difficulty)
        elif y > x:
            random_number = random.randint(x, y)
            range_of_numbers = f"{x} and {y}"
        else:
            random_number = random.randint(y, x)
            range_of_numbers = f"{y} and {x}"

        x_and_y = abs(x - y)

        if x_and_y == 1:
            limit = 1

        else:
            for limit in range(0, x_and_y + 1):
                if 2 ** limit >= x_and_y:
                    break

    print(f".:{difficulty.upper()} MODE:.")
    print(f"Guess a number between {range_of_numbers}. You have {limit} guesses.")
    attempts = 0

    for countdown in range(limit, -1, -1):

        if countdown == 0:
            print(f"Sorry, you didn't guess the number. It was {random_number}.")
            break

        guess = int(input(f"You have {countdown} guesses left: "))
        attempts += 1

        if guess == random_number:
            print(f"Nice!, the number was {random_number} and You guessed it in {attempts} attempts!")
            break

        elif guess < random_number:
            print("Too low!")

        else:
            print("Too high!")

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


def start_game():
    while True:
        print('Select difficulty level: Easy, Medium, Hard, Custom: ')
        difficulty = str(input().casefold())

        if difficulty in ['easy', 'medium', 'hard', 'custom']:
            guess_the_number_game(difficulty)
            break
        else:
            print("Invalid answer.")


if __name__ == "__main__":
    start_game()
