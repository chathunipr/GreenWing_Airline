from config import get_db_connection

def checkGameStatus(userID, rounds):

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT total_profit, total_co2, reputation
        FROM users
        WHERE userid=%s
    """, (userID,))

    profit, co2, reputation = cur.fetchone()

    cur.close()
    conn.close()

    if co2 > 200 or reputation < 20:
        return "lose"

    if rounds >= 10:
        if profit >= 500000 and co2 <= 200 and reputation >= 20:
            return "win"
        else:
            return "lose"

    return "continue"