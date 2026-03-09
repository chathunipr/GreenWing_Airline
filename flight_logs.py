from config import get_db_connection
from datetime import datetime

def processFlight(userID, routeid, profit, co2_per_flight):

    conn = get_db_connection()
    cur = conn.cursor()

    # get latest user values
    cur.execute("""
        SELECT current_budget, total_profit, total_co2, reputation
        FROM users
        WHERE userid = %s
    """, (userID,))

    result = cur.fetchone()