from config import get_db_connection

def getUserName():
    while True:
        name = input("Enter your name: ").strip()

        if name == "":
            print("Invalid input. Name cannot be empty. Please enter again.")
        elif name.isdigit():
            print("Invalid input. Name cannot be numbers only.")
        else:
            print(f"Welcome, {name}! Let's set up your airline.")
            return name