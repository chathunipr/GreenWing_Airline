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