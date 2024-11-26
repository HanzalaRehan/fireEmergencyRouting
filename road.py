"""
Author(s): 1. Hanzala B. Rehan
Description: Representing the grid in a python script
Date created: November 26th, 2024
Date last modified: November 26th, 2024
"""

import pandas as pd  # Importing pandas for data manipulation and analysis
import ast


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
        next_states = []  # Initialize a list to hold the next states and their costs

        # Filter for rows where 'Start' matches the current state and time matches
        df_start = self.DF[(self.DF['Start'] == str(state)) & (self.DF['Time'] == time)]

        # Add the 'End' states and their corresponding costs
        for _, row in df_start.iterrows():
            end_state = ast.literal_eval(row["End"])
            cost = 100 / row["Speed"]
            next_states.append((end_state, cost))

        # Filter for rows where 'End' matches the current state and time matches
        df_end = self.DF[(self.DF['End'] == str(state)) & (self.DF['Time'] == time)]

        # Add the 'Start' states and their corresponding costs
        for _, row in df_end.iterrows():
            start_state = ast.literal_eval(row["Start"])
            cost = 100 / row["Speed"]
            next_states.append((start_state, cost))

        return next_states

