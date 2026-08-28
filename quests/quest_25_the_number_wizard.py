#!/usr/bin/python3
import random

secret = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20.")

guess = 0
while guess != secret:
    guess = int(input("Enter your guess: "))

    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print("Correct! You guessed the number!")

