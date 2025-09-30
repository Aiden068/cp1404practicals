
"""Question 1"""
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

"""Question 2"""
in_file = open("name.txt", "r")
name_read = in_file.read()
print(f"Hi {name_read}!")
in_file.close()

"""Question 3"""
with open("numbers.txt", "r") as in_file:
    line_1 = int(in_file.readline())
    line_2 = int(in_file.readline())
print(line_1 + line_2)
in_file.close()

"""Question 4"""
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)