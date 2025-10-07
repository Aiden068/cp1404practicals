import random
random_numbers = 6
i = 0
quick_picks = int(input("How many quick picks? "))
while i < random_numbers:
    i += 1
    print(random.randint(1, 45), "")