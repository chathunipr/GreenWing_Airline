from config import get_db_connection

# Checking if the player wins, loses, or continues
def checkGameStatus(userID, rounds):

    conn = get_db_connection()
    cur = conn.cursor()

# Get the player's profit, co2 emissions, and reputation from database
    cur.execute("""
        SELECT total_profit, total_co2, reputation
        FROM users
        WHERE userid=%s
    """, (userID,))

    profit, co2, reputation = cur.fetchone()

    cur.close()
    conn.close()

# Losing condition
    if co2 > 200 or reputation < 20:
        return "lose"

# Check final round and determine win or lose
    if rounds >= 10:
        if profit >= 500000 and co2 <= 200 and reputation >= 20:
            return "win"
        else:
            return "lose"

# Game continues if no end condition met
    return "continue"