colours = [["Absolute zero", "#0048ba"], ["Acid green", "#b0bf1a"], ["Alice blue", "#f0f8ff"],
           ["Alizarin crimson", "#e32636"], ["Amaranth", "#e52b50"], ["Amber", "#ffbf00"], ["Amethyst", "#9966cc"],
           ["Antique white", "#faebd7"], ["Apricot", "#fbceb1"], ["Aqua", "#00ffff"]]

for name, code in colours:
    print(name)

user_colour_choice = input("Enter a colour name from the colours above: ").capitalize()
while user_colour_choice != "":
    while user_colour_choice not in name:
        print("test1")
        user_colour_choice = input("Enter a valid colour: ").capitalize()

    for name, code in colours:

            if user_colour_choice in name:
                print(f"The colour code of {user_colour_choice} is {code}")
                user_colour_choice = input("Enter a valid colour: ").capitalize()




print("test")