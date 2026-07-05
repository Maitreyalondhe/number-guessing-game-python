import art
print(art.logo)

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

while difficulty != "easy" and difficulty != "hard":
    print("Please enter a valid difficulty.")
    difficulty = input("Choose easy or hard: ")


if difficulty == "easy":
    attempts = 10

elif difficulty == "hard":
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You guessed right! The number was {number}.")
        break

    elif guess > number:
        print("Too high")
        attempts -= 1

    elif guess < number:
        print("Too low")
        attempts -= 1

    if attempts == 0:
        print(f"You lose! The correct number was {number}")
