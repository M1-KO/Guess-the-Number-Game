# Game rules:
# A range of numbers that the player can guess from:
#     Easy - 1 to 10
#     Medium - 1 to 100
#     Hard - -500 to 500
#     Custom - Player decide a range of numbers

# How many guesses the player will get before the game is over:
# 2tothepower which is bigger than a amount of numbers e.g. range 1 to 100 - guess number = 2 ** x > 100, so here its 7

# Winning condition:
#     guessing the correct number within the given number of guesse


# Ganarating random number
import random

easy = random.randint(1, 10)
medium = random.randint(1, 100)
hard = random.randint(-500, 500)
# Custom = input("Input a range of numbers:  ")
easy_limit = 10
medium_limit = 100
hard_limit = 1000

too_high = "Your number is too high, try again"
too_low = "Your number is too low, try again"

# Choosing game mode
class GameMode:
    def __init__(self, mode, limit):
        self.mode = mode
        self.limit = limit

print('choose game mode: easy, medium, hard:')
choosing_mode = str(input())
if choosing_mode == "easy":
    generated_number = easy
if choosing_mode == "medium":
    generated_number = medium
if choosing_mode == "hard":
    generated_number = hard

number = generated_number


limiter = 1
guess = int(input("Input a number: "))

if guess == number:
    print(f"Perfect! The number was {number} and You guessed it in your first try!")
    exit()

while guess != number:
    if guess > number:
        print(too_high)
        guess = int(input("Input a number: "))
    if guess < number:
        print(too_low)
        guess = int(input("Input a number: "))
else:
    print(f"Nice, You guessed it! The number was {number}!")
