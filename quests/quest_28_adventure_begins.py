#!/usr/bin/env python3

def forest():
    print("You are in a dark forest.")
    choice = input("Go LEFT or RIGHT? ").lower()
    if choice == "left":
        print("You find treasure! YOU WIN!")
    else:
        print("A bear attacks! GAME OVER.")

def castle():
    print("You're at a castle.")
    choice = input("Help the guard or STEAL? ").lower()
    if choice == "help":
        print("You become a knight! YOU WIN!")
    else:
        print("Guards catch you! GAME OVER.")

def start():
    print("Choose a place: FOREST or CASTLE?")
    place = input().lower()
    if place == "forest":
        forest()
    else:
        castle()

start()
