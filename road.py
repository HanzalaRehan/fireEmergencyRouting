"""
Author(s): 1. Hanzala B. Rehan
Description: Representing the grid in a python script
Date created: November 26th, 2024
Date last modified: November 26th, 2024
"""

import pandas as pd  # Importing pandas for data manipulation and analysis


class Roads:
    def __init__(self, path="traffic.csv"):
        """
        Desc: Initializes the Roads class by loading road segment data from a CSV file,
              renaming relevant columns, and filtering out blocked road segments.
        Parameters:
            path (str): The path to the CSV file containing traffic data.
        """
        self.DF = pd.read_csv(path)  # Load the traffic data from the CSV file
        # Rename columns for consistency and ease of use
        self.DF.rename(columns={'Road Segment Start': 'Start',
                                'Road Segment End': 'End',
                                "Current Speed (km/h)": "Speed"},
                       inplace=True)
        # Filter out rows where the road segment is blocked
        self.DF = self.DF[self.DF['Status'] != 'Blocked']

    def get_next_states(self, state, time):
        """
        Desc: Retrieves possible next states (road segments) from the current state at a given time.
        Parameters:
            state (str): The current road segment start point.
            time (str): The specific time for filtering road data.
        Returns:
            next_states (list): A list of tuples containing the end state and cost of traveling to it.
                                Each tuple is in the form (state, cost).
        """
        # Filter the DataFrame for rows matching the current state and time
        df = self.DF[(self.DF['Start'] == state) & (self.DF['Time'] == time)]
        next_states = []  # Initialize a list to hold the next states and their costs
        for _, row in df.iterrows():
            state = row["End"]  # Retrieve the end state
            cost = 1 / row["Speed"]  # Calculate the cost as the inverse of speed (time taken)
            next_states.append((state, cost))  # Append the state and cost as a tuple
        return next_states
