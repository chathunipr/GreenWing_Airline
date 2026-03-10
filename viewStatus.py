from config import get_db_connection

def viewCompanyDetails(userID):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, home_airport, total_profit, reputation, total_co2, current_budget
        FROM users
        WHERE userid = %s
    """, (userID,))

    result = cursor.fetchone()

    name = result[0]
    home_airport = result[1]
    total_profit = float(result[2] or 0)
    reputation = float(result[3] or 0)
    total_co2 = float(result[4] or 0)
    budget = float(result[5] or 0)
