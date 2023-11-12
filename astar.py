import heapq

# This class represents a point in the world.
class Node:
    def __init__(self, coordinates, g_score=float('inf'), h_score=0, parent=None):
        self.coordinates = coordinates  # The location of this point
        self.g_score = g_score  # The cost to reach this point from the start
        self.h_score = h_score  # An estimate of how far this point is from the goal
        self.parent = parent  # The previous point

    # calculates the total cost of reaching the point.
    def f_score(self):
        return self.g_score + self.h_score

    # Define how instances of Node should be compared for the heapq
    def __lt__(self, other):
        return self.f_score() < other.f_score()

# finds the best path
def weighted_a_star(graph, start, goal, heuristic, weights):
    open_set = []  # Points to be explored
    closed_set = set()  # Points already explored

    # Create a starting point and add it to the list of points to explore.
    start_node = Node(start, 0, heuristic(start, goal), None)
    heapq.heappush(open_set, start_node)

    # Keep exploring until there are no more points to explore.
    while open_set:
        # Get the point with the lowest total cost from the list of points to explore.
        current_node = heapq.heappop(open_set)

        # If the goal is reached, then the best path has been found!
        if current_node.coordinates == goal:
            path = []
            while current_node:
                path.append(current_node.coordinates)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get it from the start to the goal

        closed_set.add(current_node.coordinates)

        # Explore neighboring points and see if there's a better path
        neighbors = get_neighbors(graph, current_node.coordinates)
        if neighbors is not None:
            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue

                tentative_g_score = current_node.g_score + get_edge_cost(graph, current_node.coordinates, neighbor, weights)

                neighbor_node = Node(neighbor)
                if tentative_g_score < neighbor_node.g_score:
                    neighbor_node.g_score = tentative_g_score
                    neighbor_node.h_score = heuristic(neighbor, goal)
                    neighbor_node.parent = current_node

                    if neighbor_node.coordinates not in closed_set:
                        heapq.heappush(open_set, neighbor_node)

    return None  # No path found

# returns neighboring points
def get_neighbors(graph, coordinates):
    return graph.get(coordinates, [])

# returns the cost of moving from one point to another
def get_edge_cost(graph, start, end, weights):
    return graph.get((start, end), 0)

# Example usage:
graph = {
    (0, 0, 0, 0): {(1, 0, 0, 0): 1, (0, 1, 0, 0): 1},
    (1, 0, 0, 0): {(1, 1, 0, 0): 1, (0, 0, 0, 0): 1},
    (1, 1, 0, 0): {(1, 1, 1, 0): 1, (1, 0, 0, 0): 1},
    (1, 1, 1, 0): {(1, 1, 1, 1): 1},
}

start_node = (0, 0, 0, 0)
goal_node = (1, 1, 1, 1)
heuristic_function = lambda x, y: 0  # Replace with the actual heuristic function
weights = [1, 1, 1, 1]  # Replace with the actual edge weights

path = weighted_a_star(graph, start_node, goal_node, heuristic_function, weights)
print(path)
