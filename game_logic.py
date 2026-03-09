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