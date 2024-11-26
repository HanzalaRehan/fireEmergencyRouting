"""
Author(s): 1. Hanzala B. Rehan
Description: Main entry point for the program.
Date Created: November 26th, 2024.
Date Last Modified: November 26th, 2024.
"""

from road import Roads  # Importing the Roads class to handle road data
from search import astar_first_search  # Importing the A* search function
import pandas as pd  # Importing pandas for data manipulation

# Define fixed locations for fire stations
STATION1 = (1, 1)  # Coordinates for Station 1
STATION2 = (10, 10)  # Coordinates for Station 2

# List of emergency calls with their locations and time
EMERGENCY_CALLS = [
    ((5, 5), '22:00'),
    ((8, 3), '15:00'),
    ((2, 9), '12:00'),
    ((4, 4), '15:00'),
    ((7, 2), '15:00'),
    ((3, 6), '12:00'),
    ((9, 9), '3:00'),
    ((1, 8), '3:00'),
    ((10, 1), '15:00'),
    ((6, 7), '3:00')
]


def main():
    """
    Desc: Main function to process emergency calls by determining the shortest path from fire stations
          to the emergency locations using A* search and storing results in a DataFrame.
    """
    roads = Roads()  # Initialize the Roads object with traffic data

    # List to hold data for the DataFrame
    data = []

    for call in EMERGENCY_CALLS:
        loc = call[0]  # Location of the emergency
        time = call[1]  # Time of the emergency

        try:
            time1, path1 = astar_first_search(roads, STATION1, loc, time)
        except Exception:
            time1, path1 = "Traffic Blocked", None

        try:
            time2, path2 = astar_first_search(roads, STATION2, loc, time)
        except Exception:
            time2, path2 = "Traffic Blocked", None

        # Determine the preferred station based on time
        if isinstance(time1, str):  # If Station 1 is blocked
            preferred_station = "Fire Station 2"
        elif isinstance(time2, str):  # If Station 2 is blocked
            preferred_station = "Fire Station 1"
        else:
            preferred_station = "Fire Station 1" if time1 < time2 else "Fire Station 2"

        # Append the data to the list
        data.append({
            "Emergency Location": loc,
            "Time": time,
            "Preferred Station": preferred_station,
            "Time from Station 1": str(time1),
            "Time from Station 2": str(time2)
        })

    # Create a pandas DataFrame from the collected data
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df)

    # Optionally, save the DataFrame to a CSV file
    df.to_csv("emergency_calls_summary.csv", index=False)


if __name__ == "__main__":
    main()
