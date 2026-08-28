#!/usr/bin/python3
def ask_for_age():
    x=int(input("Enter your age: "))
    return x 
y=ask_for_age()
def can_they_vote():
    if y>18:
        print("They can vote")
    else:
        print("You are not yet eligible to vote")
can_they_vote()
