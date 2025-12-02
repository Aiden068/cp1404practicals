

def main():
    name_from_email = {}
    email = input("Email: ")
    while email != "":
        name = name_to_email(email)
        yes_or_no = input(f"Is your name {name}? ").upper()
        if yes_or_no != "Y" and yes_or_no != "":
            name = input("Name: ")
        name_from_email[email] = name
        email = input("Email: ")

    for email, name in name_from_email.items():
        print(f"{name} ({email})")


def name_to_email(email):
    symbal = email.split("@")[0]
    parts = symbal.split(".")
    name = " ".join(parts)
    return name

main()

