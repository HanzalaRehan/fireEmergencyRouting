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
          A* uses a combination of the actual path cost and a heuristic to efficiently find the optimal solution.
    Parameters:
        road (Roads): An instance of the Roads class.
        start (tuple): The starting position as (row, col).
        goal (tuple): The goal position as (row, col).
        time (str): time of emergency, format: hr:mm.
    returns:
        (tuple): Total path cost from start to goal, and a list of all intersections taken.
    """
    start = CostNode(state=start, parent=None, cost=0)  # Cost is initialized to 0
    func = cumulative_cost_function
    frontier = PriorityQueueFrontier(func, goal)  # Frontier with priority queue
    frontier.add(start)

    explored_states = set()

    while True:
        if frontier.empty():
            raise Exception("No solution")

        node = frontier.remove()

        if node.state == goal:
            path = []
            path_cost = 0
            while node.parent is not None:
                path.append(node.state)
                path_cost += node.cost
                node = node.parent
            path.reverse()
            return path_cost, path

        explored_states.add(node.state)

        for state, cost in road.get_next_states(node.start, time):
            if not frontier.contains_state(state) and state not in explored_states:
                child = CostNode(state=state, parent=node, cost=cost)
                frontier.add(child)
