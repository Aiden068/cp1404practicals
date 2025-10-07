"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def print_report(amount_of_months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, amount_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))




def main():
    """Display income report for incomes over a given number of amount_of_months."""
    incomes = []
    amount_of_months = int(input("How many amount_of_months? "))

    for month in range(1, amount_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(amount_of_months, incomes)


main()