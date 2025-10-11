import random
number_of_columns = 6
i = 0
quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    numbers = []
    while len(numbers) < number_of_columns:
        random_number = random.randint(1, 45)

    # list1 = list1.append(random.randint(1, 45))
        if random_number not in numbers:
            numbers.append(random_number)
    print(" ".join(str(f"{number:3}") for number in numbers))
