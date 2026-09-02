# Number Guessing Game

import random

secret_number = random.randint(1, 50)
attempts = 0

print("================================")
print("       NUMBER GUESSING GAME")
print("================================")
print("Guess a number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("\nCongratulations!")
        print("You guessed the correct number.")
        print("Number of attempts:", attempts)
        break