from config import get_db_connection
from game_logic import checkGameStatus
from invesments import investGreenTech
from users import getUserName, chooseHomeAirport, createUser
from routes import chooseRoute
from viewStatus import viewCompanyDetails


def displayIntro():
    print("="*60)
    print("🌿 WELCOME TO GREENWING AIRLINES: ECO-TYCOON 🌿")
    print("="*60)

    print("\nCongratulations! You are the newly appointed CEO of GreenWing Airlines.")
    print("Your mission is to build a profitable airline while protecting the planet.")
    print("-"*60)

    while True:
        choice = input("\nPress 1 to see Game Rules and Objectives: ")

        if choice == "1":
            break
        else:
            print("Invalid input. Please press 1 to continue.")

    print("\nGAME RULES & OBJECTIVES")
    print("-"*60)
    print("1. Starting Budget      : $250,000")
    print("2. Starting Reputation  : 75%")
    print("3. Starting CO2 Emission: 0 tons")
    print("4. The game is played in ROUNDS.")
    print("5. You can play a maximum of 10 rounds.")
    print("6. In each round you must make strategic decisions to balance:")
    print("   💰 Profit")
    print("   🌍 Environmental impact")
    print("   ⭐ Company reputation")

    while True:
        choice = input("\nPress 1 to see How to Win the Game: ")

        if choice == "1":
            break
        else:
            print("Invalid input. Please press 1 to continue.")

    print("\nHOW TO WIN")
    print("-"*60)
    print("You must achieve ALL of the following before the game ends:")
    print("  💰 Total Profit : Earn at least $500,000")
    print("  ⭐ Reputation   : Keep reputation at 20% or higher")
    print("  🌍 Total CO2    : Maintain 200 tons or less")

    while True:
        choice = input("\nPress 1 to see How to Play the Game: ")

        if choice == "1":
            break
        else:
            print("Invalid input. Please press 1 to continue.")

    print("\nHOW TO PLAY")
    print("-"*60)
    print("Each round you can choose one of the following actions:")
    print(" [1] Fly a Route")
    print("      Choose from 5 random destinations.")
    print("      Flights generate profit but also produce CO2.")

    print("  [2] Invest in GreenTech")
    print("      Spend money to reduce CO2 emissions and increase reputation.")

    print("  [3] View Company Status")
    print("      Check your latest profit, reputation, and total CO2 emissions.")

    print("  [4] Exit")
    print("      Leave the game.")

    print("\n⚠ IMPORTANT:")
    print("If your CO2 exceeds 200 tons OR your reputation drops below 20%,")
    print("your airline will fail environmental regulations and you lose the game.")

    print("\nThe game will last up to 10 rounds, so plan your strategy carefully!")

    print("="*60)

    input("\nPress 1 to start the game: ")
    print("Initializing... Good luck CEO! ✈🌍")

def displayDashboard(userid):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, home_airport, current_budget, reputation, total_co2
        FROM users
        WHERE userid = %s
    """, (userid,))
    result = cursor.fetchone()

    if result:
        name, homeAirport, budget, reputation, total_co2 = result
        print("🌿 COMPANY DASHBOARD 🌿")
        print("=" * 60)
        print(f"CEO Name       : {name}")
        print(f"Home Airport   : {homeAirport}")
        print(f"Budget         : ${budget}")
        print(f"Reputation     : {reputation}%")
        print(f"Total CO2      : {total_co2} tons")

    cursor.close()
    conn.close()

def mainMenu(userID):

    rounds = 0

    while True:
        print("\nChoose an option")
        print("1. Choose a route")
        print("2. Invest in Greentech")
        print("3. View Company status")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == "1":

            rounds += 1

            chooseRoute(userID, rounds)

            status = checkGameStatus(userID, rounds)

            if status == "win":
                print("\nCONGRATULATIONS! YOU WON THE GAME! You have built a profitable and a sustainable airline")
                break

            if status == "lose":
                print("\nGAME OVER! Your company failed environmental regulations.")
                break

        elif choice == "2":
            investGreenTech(userID)

        elif choice == "3":
            viewCompanyDetails(userID)

        elif choice == "4":
            print("\nReturning to instructions page...\n")
            displayIntro()

def main():
    displayIntro()
    userName = getUserName()
    homeAirport = chooseHomeAirport()
    userID = createUser(userName, homeAirport)

    displayDashboard(userID)
    mainMenu(userID)

if __name__ == "__main__":
    main()