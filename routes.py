from config import get_db_connection
from datetime import datetime
from flight_logs import processFlight

def chooseRoute(userID):
    while True:
        conn = get_db_connection()
        cur = conn.cursor()

        print("Available Routes:")
        print("-"*50)

        # Fetch 5 random routes
        cur.execute("""
            SELECT routeid, name, location, longitude_deg, latitude_deg, airport_fee, fuel_cost, passengers, co2_per_flight, ticket_price
            FROM routes
            ORDER BY RAND()
            LIMIT 5
        """)
        routes = cur.fetchall()

        for i, route in enumerate(routes, start=1):
            routeid = route[0]
            name = route[1]
            location = route[2]
            longitude_deg = float(route[3])
            latitude_deg = float(route[4])
            distance = abs(latitude_deg * longitude_deg)
            print(f"{i}. {name}, {location} ({round(distance)} km)")

        print("0 - Return to main menu")