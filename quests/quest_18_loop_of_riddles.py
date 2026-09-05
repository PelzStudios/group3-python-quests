#!/usr/bin/env python3

secret = 42 
guess = 0

while guess != secret:
    guess = int(input("Guess the number in range 1-100: "))
    print("Won!" if guess == secret else "Too low" if guess < secret else "Too high")
