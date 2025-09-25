"""Enter score"""
def get_choice():
    score = int(input("Enter score: "))
    return score

"""Get grade from score"""
def print_choice(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

"""Print stars based on score"""
def show_choice(score):
    print("*" * score)

"""Menu and choice input"""
def main():
    score = None
    choice = ""
    while choice != "q":
        choice = input("(G)et a valid score (must be 0-100 inclusive)\n(P)rint result (copy or import your function to determine the result from score.py)\n(S)how stars (this should print as many stars as the score)\n(Q)uit").lower()
        if choice == "g":
            score = get_choice()
        elif choice == "p":
            if score is None:
                print("Enter a score first")
            else:
                print_choice(score)
        elif choice == "s":
            if score is None:
                print("Enter a score first")
            else:
                show_choice(score)
        elif choice == "q":
            print("Goodbye")
        else:
            print("Incorrect, try again")
            choice = input(
                "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result (copy or import your function to determine the result from score.py)\n(S)how stars (this should print as many stars as the score)\n(Q)uit").lower()

main()
