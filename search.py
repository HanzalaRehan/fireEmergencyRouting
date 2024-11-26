"""
Author(s):  1. Hanzala B. Rehan
Description: Uses BFS, DFS, Greedy and A* Search.
Date created: November 26th, 2024
Date last modified: November 26th, 2024
"""

from util import CostNode, PriorityQueueFrontier, manhattan_distance,\
    cumulative_cost_function
from road import Roads


def astar_first_search(road, start, goal, time):
    """
    Desc: Implements A* Search to find the shortest path in the maze.
    Parameters:
        road (Roads): An instance of the Roads class.
        start (str): The starting road segment.
        goal (str): The goal road segment.
        time (str): Time of the search, format: hr:mm.
    Returns:
        (tuple): Total path cost from start to goal, and a list of all intersections taken.
    """
    start_node = CostNode(state=start, parent=None, cost=0)
    func = cumulative_cost_function
    frontier = PriorityQueueFrontier(func, goal)
    frontier.add(start_node)

    explored_states = set()

    while True:
        if frontier.empty():
            raise Exception("No solution found")

        node = frontier.remove()

        if node.state == goal:
            path = []
            cost = node.cost
            while node.parent is not None:
                path.append(node.state)
                node = node.parent
            path.reverse()
            return cost, path  # Return the final cost from the goal node

        explored_states.add(node.state)

        for state, cost in road.get_next_states(node.state, time):
            if state not in explored_states and not frontier.contains_state(state):
                child = CostNode(state=state, parent=node, cost=node.cost + cost)
                frontier.add(child)
