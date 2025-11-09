FILENAME = "projects.txt"
placeholder = 5

def main():
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {placeholder} projects from {FILENAME}")
    choice = (input("- (L)oad projects\n"
"- (S)ave projects\n"
"- (D)isplay projects\n"
"- (F)ilter projects by date\n"
"- (A)dd new project\n"
"- (U)pdate project\n"
"- (Q)uit\n"
">>> ")).lower()

    while choice != "q":
        if choice == "s":
            save_projects()
        elif choice == "d":
            display_projects()
        elif choice == "f":
            filter_projects()
        elif choice == "a":
            add_project()
        elif choice == "u":
            update_project()
        else:
            print("Please enter a valid option")
            choice = (input("- (L)oad projects\n"
                            "- (S)ave projects\n"
                            "- (D)isplay projects\n"
                            "- (F)ilter projects by date\n"
                            "- (A)dd new project\n"
                            "- (U)pdate project\n"
                            "- (Q)uit\n"
                            ">>> ")).lower()
    if_save = input("Would you like to save to projects.txt?")

    print("Thank you for using custom-built project management software.")








def save_projects():
    pass

def display_projects():
    pass

def filter_projects():
    pass

def add_project():
    pass

def update_project():
    pass


main()