"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint

def parameter():


    return()








def random_number():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

    random_score = randint(0, 100)
    if random_score < 0 or random_score > 100:
        print("Invalid score")
    elif random_score >= 90:
        print("Excellent")
    elif random_score >= 50:
        print("Passable")
    else:
        print("Bad")


random_number()