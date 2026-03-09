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

    current_budget = float(result[0])
    total_profit = float(result[1])
    total_co2 = float(result[2])
    reputation = float(result[3])

    # update values
    new_budget = current_budget + profit
    new_total_profit = total_profit + profit
    new_total_co2 = total_co2 + co2_per_flight

    # reputation loss from pollution
    reputation_loss = co2_per_flight * 0.25
    new_reputation = reputation - reputation_loss