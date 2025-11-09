
from prac_06.guitar import Guitar

guitars = []
def main():
    print("My guitars!")
    name = input(f"Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        if_vintage = ""
        if guitar.is_vintage():
            if_vintage = "(Vintage)"
        print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, if_vintage))

main()
