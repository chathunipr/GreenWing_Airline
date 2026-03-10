from config import get_db_connection
def investGreenTech(userID):

    conn = get_db_connection()
    cursor = conn.cursor()

    # get current user values
    cursor.execute("""
        SELECT current_budget, total_co2, reputation
        FROM users
        WHERE userid = %s
    """, (userID,))

    result = cursor.fetchone()

    current_budget = float(result[0])
    total_co2 = float(result[1])
    reputation = float(result[2])

    print("\nYour Current Budget:", current_budget)
    while True:

        amount_input = input("Enter amount to invest in Green Tech: ")

        if amount_input.isdigit():

            amount = float(amount_input)

            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")

            elif amount > current_budget:
                print("You do not have enough budget for this investment.")

            else:
                break

        else:
            print("Invalid input. Please enter numbers only.")

        # calculate benefits
    co2_reduced = amount / 10000
    reputation_increased = amount / 20000

    # update values
    new_budget = current_budget - amount
    new_total_co2 = max(0, total_co2 - co2_reduced)
    new_reputation = reputation + reputation_increased

    # prevent CO2 going below zero
    # if new_total_co2 < 0:
    #     new_total_co2 = 0