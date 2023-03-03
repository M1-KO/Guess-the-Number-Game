# # Game rules:
# # A range of numbers that the player can guess from:
# #     Easy - 1 to 10
# #     Medium - 1 to 100
# #     Hard - -500 to 500
# #     Custom - Player decide a range of numbers
#
# # How many guesses the player will get before the game is over:
# # 2tothepower which is bigger than a amount of numbers e.g. range 1 to 100 - guess number = 2 ** x > 100, so here its 7
#
# # Winning condition:
# #     guessing the correct number within the given number of guesse
#
#
# # Ganarating random number
# import random
#
# # easy = random.randint(1, 10)
# medium = random.randint(1, 100)
# hard = random.randint(-500, 500)
# # Custom = input("Input a range of numbers:  ")
# easy_limit = 10
# medium_limit = 100
# hard_limit = 1000
#
# def easy(mode, counter):
#     mode = random.randint(1, 10)
#     counter = 4
#
#
#
# too_high = "Your number is too high, try again"
# too_low = "Your number is too low, try again"
#
# # Choosing game mode
# class GameMode:
#     def __init__(self, mode, limit):
#         self.mode = mode
#         self.limit = limit
#
# print('choose game mode: easy, medium, hard:')
# choosing_mode = str(input())
# if choosing_mode == "easy":
#     generated_number = easy
# if choosing_mode == "medium":
#     generated_number = medium
# if choosing_mode == "hard":
#     generated_number = hard
#
# number = generated_number
#
#
# guess = int(input("Input a number: "))
#
# if guess == number:
#     print(f"Perfect! The number was {number} and You guessed it in your first try!")
#     exit()
#
# while guess != number:
#     if guess > number:
#         print(too_high)
#         counter -= 1
#         guess = int(input("Input a number: "))
#     if guess < number:
#         print(too_low)
#         guess = int(input("Input a number: "))
# else:
#     print(f"Nice, You guessed it! The number was {number}!")
#


# import random


# def easy():
#     if game_mode == "easy":
#       easy_mode = random.randint(1, 10)
#       counter = 4
#
#
# game_mode = str(input('choose game mode: easy, medium, hard:'))
#
# number = game_mode
#
#
# guess = int(input("Input a number: "))
#
# if guess == number:
#     print(f"Perfect! The number was {number} and You guessed it in your first try!")
#     exit()
#
# while guess != number:
#     if guess > number:
#         print(too_high)
#         counter -= 1
#         guess = int(input("Input a number: "))
#     if guess < number:
#         print(too_low)
#         guess = int(input("Input a number: "))
# else:
#     print(f"Nice, You guessed it! The number was {number}!")
#
# import random
#
#
#
# def guess_the_number_game(difficulty):
#     if difficulty == 'easy' or difficulty == "Easy":
#         number = random.randint(1, 10)
#         limiter = 4
#     elif difficulty == 'medium' or difficulty == "Medium":
#         number = random.randint(1, 50)
#         limiter = 6
#     elif difficulty == 'hard':
#         number = random.randint(1, 100)
#         limiter = 8
#     else:
#         print("Invalid difficulty level.")
#         return
#
#     print(".:Welcome to Guess the Number Game!:.")
#
#     print('Select difficulty level: Easy, Medium, Hard: ')
#     difficulty = str(input())
#
#     for i in range(1, limiter + 1):
#         guess = int(input(f"Guess #{i}: "))
#
#         if guess == number:
#             print(f"Congratulations, you guessed the number in {i} tries!")
#             return
#
#         elif guess < number:
#             print("Too low!")
#
#         else:
#             print("Too high!")
#
#     print(f"Sorry, you didn't guess the number. It was {number}. Better luck next time!")
#
# guess_the_number_game()

import random

print(".:Welcome to Guess the Number Game:.")

print('Select difficulty level: Easy, Medium, Hard: ')
difficulty = str(input()).casefold()


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
    else:
        print("Invalid difficulty level.")
        return

    print(f"{difficulty.capitalize()} mode")
    print(f"Guess a number between {range_of_numbers}. You have {limit} guesses.")
    attempts = 0

    for countdown in range(limit, 0, -1):
        guess = int(input(f"You have {countdown} guesses left: "))
        attempts += 1

        if guess == random_number:
            print(f"Nice!, the number was {random_number} and You guessed it in {attempts} attempts!")
            continue

        elif guess < random_number:
            print("Too low!")

        else:
            print("Too high!")

    print(f"Sorry, you didn't guess the number. It was {random_number}.")
    print("")
    print("Do you want to play again? Yes/No")

    answer = str(input()).casefold()

    if answer == "yes":

        guess_the_number_game(difficulty)


guess_the_number_game(difficulty)
