
def main():
    MIN_LENGTH = 8
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print("Error, try again")
        password = input("Enter password: ")
    print("* " * len(password))

main()