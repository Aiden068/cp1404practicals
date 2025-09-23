
def main():
    MIN_LENGTH = 8
    get_password = input("Enter password: ")
    while len(get_password) < MIN_LENGTH:
        print("Error, try again")
        get_password = input("Enter password: ")
    print("* " * len(get_password))

main()