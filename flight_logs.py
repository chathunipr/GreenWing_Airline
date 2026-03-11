# import the database connection function from config file
from config import get_db_connection

# import datetime to generate a unique flight id using time
from datetime import datetime

# function to calculate new values, update the database and return new calculated values
# parameters: userID, routeid, profit earned from flight, and CO2 produced
# return values: profit, new_budget, new_total_co2, new_reputation
def processFlight(userID, routeid, profit, co2_per_flight):

    conn = get_db_connection() #create database connection
    cur = conn.cursor() #create cursor to execute SQL queries

    # get the latest financial and environmental values of the user
    cur.execute("""
        SELECT current_budget, total_profit, total_co2, reputation
        FROM users
        WHERE userid = %s
    """, (userID,))

    result = cur.fetchone()

    # convert values into float for calculations
    current_budget = float(result[0])
    total_profit = float(result[1])
    total_co2 = float(result[2])
    reputation = float(result[3])

    # calculate new updated values
    new_budget = current_budget + profit
    new_total_profit = total_profit + profit
    new_total_co2 = total_co2 + co2_per_flight

    # calculate reputation loss from pollution
    reputation_loss = co2_per_flight * 0.25
    new_reputation = reputation - reputation_loss

    # if reputation value gets (-); assign to zero (0)
    if new_reputation < 0:
        new_reputation = 0

    # update users table with new calculated values
    cur.execute("""
                UPDATE users
                SET current_budget=%s,
                    total_profit=%s,
                    total_co2=%s,
                    reputation=%s
                WHERE userid = %s
                """, (new_budget, new_total_profit, new_total_co2, new_reputation, userID))

    # create unique flight id
    timestamp = datetime.now().strftime("%H%M%S")
    flight_id = str(userID) + "" + str(routeid) + "" + timestamp

    # save the completed flight record into flight_logs table
    cur.execute("""
                INSERT INTO flight_logs
                    (flight_id, userid, routeid, profit_generated, co2_produced)
                VALUES (%s, %s, %s, %s, %s)
                """, (flight_id, userID, routeid, profit, co2_per_flight))

    conn.commit() # save all database changes
    cur.close() # close cursor
    conn.close() # close database connection

    return profit, new_budget, new_total_co2, new_reputation