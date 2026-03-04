import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="12345678",
    database="greenwing"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM routes LIMIT 5")
results = cursor.fetchall()

for row in results:
    print(row)

connection.close()

def displayIntro():
    print("="*60)
    print("🌿WELCOME TO GREENWING AIRLINES: ECO-TYCOON🌿")
    print("="*60)
    print("\nCongratulations! You are the new CEO of GreenWing Airlines.")
    print("Your mission: Build a profitable airline while saving the planet.")
    print(f"{'-'*60}")

    while True:
        choice = input("\nPress 1 to see Game Rules and Objectives: ")
        if choice == "1":
            print("\nGAME RULES & OBJECTIVES:")
            print(f"1. Starting budget: $500,000")
            print(f"2. Starting reputation: 75%")
            print(f"3. Starting CO2 Emissions: 0 tons")
            break
        else:
            print("\nInvalid input. Please press 1 to continue.")

    while True:
        choice = input("\nPress 1 to see How to Win: ")
        if choice == "1":
            print("\nHOW TO WIN:")
            print("Reach the following targets simultaneously:")
            print("  💰 Total Profit: Earn $1,000,000")
            print("  ⭐ Reputation: Gain At least 20% or more")
            print("  🌍 Total CO2: Maintain 500 tons or less")
            break
        else:
            print("\nInvalid input. Please press 1 to continue.")

    while True:
        choice = input("\nPress 1 to see How to Play: ")
        if choice == "1":
            print("\nHOW TO PLAY:")
            print("Each round, you choose from 4 options:")
            print("  [1] Fly a Route: Choose from 5 random destinations. Earn profit but emit CO2.")
            print("  [2] Invest in GreenTech: Spend money to reduce your CO2 and boost reputation.")
            print("  [3] View Company status: Check your lifetime flight history and performance.")
            print("  [4] Exit: Close the game.")

            print(f"\n{'-' * 60}")
            print("Careful! If your CO2 exceeds 500 tons OR Reputation falls below 20%!, you lose the game!")
            print("=" * 60)
            break
        else:
            print("Invalid input. Please press 1 to continue.")

    while True:
        choice = input("\nPress 1 to start the game: ")
        if choice == "1":
            print("Initializing Hangar... Good luck!!")
            break
        else:
            print("\nInvalid input. Please press 1 to start the game!.")

displayIntro()
