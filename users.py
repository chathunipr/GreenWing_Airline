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


def chooseHomeAirport():
    airports = [
        "1. Bandaranaike International Airport (CMB), Sri Lanka",
        "2. Dubai International Airport (DXB), UAE",
        "3. Heathrow Airport (LHR), UK",
        "4. Helsinki Airport (HEL), Finland",
        "5. Changi Airport (SIN), Singapore"
    ]
    print("\nPlease choose your home from the list below: ")
    for airport in airports:
        print(airport)

    while True:
        choice = input("\nEnter the number of your home airport (1-5): ")
        if choice in ["1", "2", "3", "4", "5"]:
            chosenAirport = airports[int(choice) - 1]  #fixed index
            print(f"\nGreat! Your home airport is set to: {chosenAirport}")
            return chosenAirport
        else:
            print("Invalid input. Please enter a number between 1-5.")


def createUser(name, home_airport):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO users (name, home_airport, current_budget, reputation, total_co2, total_profit)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (name, home_airport, 250000, 75, 0, 0))
    conn.commit()

    user_id = cursor.lastrowid
    print("User created successfully!")

    cursor.close()
    conn.close()
    return user_id



