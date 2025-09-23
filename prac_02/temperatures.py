"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
"""Convert celsius to fahrenheit"""
def convert_c_to_f():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")
    return()

""" Convert fahrenheit to celsius"""
def convert_f_to_c():
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")
    return()

"""Main function"""
def main():
    menu = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_c_to_f()
        elif choice == "F":
            convert_f_to_c()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")

main()