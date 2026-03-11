from config import get_db_connection

def viewCompanyDetails(userID):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, home_airport, total_profit, reputation, total_co2, current_budget
        FROM users
        WHERE userid = %s
    """, (userID,))

    result = cursor.fetchone()

    name = result[0]
    home_airport = result[1]
    total_profit = float(result[2] or 0)
    reputation = float(result[3] or 0)
    total_co2 = float(result[4] or 0)
    budget = float(result[5] or 0)

    print("\n")
    print("=" * 50)
    print("     GREENWING AIRLINES - COMPANY STATUS")
    print("=" * 50)

    print("CEO:", name)
    print("Home Airport:", home_airport)

    print("-" * 50)

    print("Current Budget: $", round(budget, 2))
    print("Total Profit: $", round(total_profit, 2))
    print("Reputation:", round(reputation, 2), "%")
    print("Total CO2 Emission:", round(total_co2, 2))

    print("=" * 50)


# validation loop
    while True:
        choice = input("\nPress 0 to return to Main Menu: ")

        if choice == "0":
            break
        else:
            print("Invalid input. Please press 0 to return.")

    cursor.close()
    conn.close()





