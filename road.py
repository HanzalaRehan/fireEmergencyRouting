"""
Authors: (1) Hanzala B. Rehan
Description: Representing the grid in a python script
Date created: November 26th, 2024
Date last modified: November 26th, 2024
"""

from util import CostNode
import pandas as pd


class Roads:
    def __init__(self, path="traffic.csv"):
        self.DF = pd.read_csv("traffic.csv")
        self.DF.rename(columns={'Road Segment Start': 'Start', 'Road Segment End': 'End', "Current Speed (km/h)": "Speed"}, inplace=True)
        self.DF = self.DF[self.DF['Status'] != 'Blocked']

    def get_next_states(self, state, time):
        # Filter the DataFrame for the given state and time
        df = self.DF[(self.DF['Start'] == state) & (self.DF['Time'] == time)]
        next_states = []
        for _, row in df.iterrows():
            state = row["End"]
            cost = 1 / row["Speed"]
            next_states.append((state, cost))
