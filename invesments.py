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
    # count previous investments
    cursor.execute(
        "SELECT COUNT(*) FROM investments WHERE userid = %s",
        (userID,)
    )

    count = cursor.fetchone()[0]

    # create investment id
    investment_id = str(userID) + "INV" + str(count + 1)

    # insert investment record
    cursor.execute("""
                   INSERT INTO investments
                   (investmentid, userid, amount, co2_reduced, reputation_increased, investment_time)
                   VALUES (%s, %s, %s, %s, %s, NOW())
                   """, (investment_id, userID, amount, co2_reduced, reputation_increased))

    # update user values
    cursor.execute("""
                   UPDATE users
                   SET current_budget = %s,
                       total_co2      = %s,
                       reputation     = %s
                   WHERE userid = %s
                   """, (new_budget, new_total_co2, new_reputation, userID))

    conn.commit()

    print("\nInvestment Successful!")
    print("-" * 40)
    print("Amount Invested:", amount)
    print("Updated Budget:", round(new_budget, 2))
    print("CO2 Reduced:", round(co2_reduced, 2))
    print("Reputation increased:", round(reputation_increased, 2))
    print("Updated Total CO2:", round(new_total_co2, 2))
    print("Updated Reputation:", round(new_reputation, 2), "%")

    cursor.close()
    conn.close()