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

        while True:
            choice = input("Enter your preferred route (1-5) or 0 to return: ")

            if not choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            choice = int(choice)

            if choice == 0:
                cur.close()
                conn.close()
                return

            if 1 <= choice <= 5:
                i = choice - 1
                selected = routes[i]
                break
            else:
                print("Invalid input. Please choose between 1 and 5.")

                # Extract route details
        routeid, name, location, longitude_deg, latitude_deg, airport_fee, fuel_cost, passengers, co2_per_flight, ticket_price = selected
        longitude_deg = float(longitude_deg)
        latitude_deg = float(latitude_deg)
        airport_fee = float(airport_fee or 0)
        fuel_cost = float(fuel_cost or 0)
        passengers = int(passengers or 0)
        co2_per_flight = float(co2_per_flight or 0)
        ticket_price = float(ticket_price or 0)

        distance = abs(latitude_deg * longitude_deg)

        # fixed rates
        c02Rate = 0.05
        fuelRate = 8

        # calculate fuel and CO2
        fuel_cost = distance * fuelRate
        co2_per_flight = distance * c02Rate

        # calculate revenue and profit
        revenue = passengers * ticket_price
        profit = revenue - fuel_cost - airport_fee

        # fetch home airport
        cur.execute("SELECT home_airport FROM users WHERE userid = %s", (userID,))
        home_airport = cur.fetchone()[0]

        print("\nRoute Details")
        print("-" * 40)
        print(f"Route: {home_airport.split('. ')[1]} ---> {name}")
        print()
        print("Location:", location)
        print("Distance:", round(distance, 2), "km")
        print("Fuel Cost:", round(fuel_cost, 2))
        print("Airport Fee:", round(airport_fee, 2))
        print("Passenger Demand:", passengers)
        print("Ticket Price:", ticket_price)
        print()
        print("Estimated CO2 Emission:", round(co2_per_flight, 2))
        print("Estimated Revenue:", round(revenue, 2))
        print("Estimated Profit:", round(profit, 2))

        cancel_flight = False

        while True:
            confirm = input("Confirm this flight? (y/n): ").lower()

            if confirm == "y":
                break
            elif confirm == "n":
                print("Flight cancelled. Returning to route selection...\n")
                cancel_flight = True
                break
            else:
                print("Invalid input. Please enter y or n.")

        if cancel_flight:
            cur.close()
            conn.close()
            continue

        profit, new_budget, new_total_co2, new_reputation = processFlight(
            userID,
            routeid,
            profit,
            co2_per_flight
        )


