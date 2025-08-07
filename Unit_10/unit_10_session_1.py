

# Problem 1: Graphing Flights

# Understand
# What should we return when the graph does not have node?
# Are we dealing with directed or indirected graph?
# Is each key unique?
# Is there a time or space complexity constraint?

# Plan
# Create a dictionary called flight that will stores name of Airport as keys and their connected neighbor as values.
# print flight.

# Implement

flights = {
    "JFK": ["LAX", "DFW"],
    "LAX" : "JFK",
    "DFW" : ["JFK", "ATL"],
    "ATL" : "DFW"
}

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])



# Problem 2: There and Back

# Understand
# What should we return when the graph does not have node?
# Are we working with directed or indirected graph?
# Is each key unique?
# Is there a time or space complexity constraint?

# Plan
# Use a nested loop using two variables i and j. where i will be use for the outer loop and j the inner loop.
# Iterate over each destination i.
# Iterate over each destination of j reachable from i.
# Return False, if there is no a flight back from j to i, 
# Return True, after checking all destinations.

# Implement
def bidirectional_flights(flights):
    """eturns True if for any flight from a destination i to a destination j there also exists a flight from destination j to destination i.
      Return False otherwise."""
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))



# Problem 3: Find Center of Airport
# Understand
# WHat is the center of the airport?
# Is there a time or space complexity that we should be aware of?
# What should we when there is tie?

# Plan
# Define an empty dictionary to store the number of connections for each terminal.
# Iterate through the list of terminals and for each terminal, check if it is connected to any other terminal.
# If it is, increment the count for that terminal in the dictionary.
# Iterate over the dictionary and find the terminal with the maximum count.
# Return that terminal as the center of the airport.
# time complexity is O(N) where N is the number of nodes.
# space complexity is O(N).

# Implement

def find_center(terminals):
    """ Function that return the center of the given airport."""
    count = {}

    for u, v in terminals:
        count[u] = count.get(u, 0) + 1
        count[v] = count.get(v, 0) + 1

    for terminal, c in count.items():
        if c > 1:
            return terminal


terminals1 = [[1, 2], [2, 3], [4, 2]]
terminals2 = [[1, 2], [5, 1], [1, 3], [1, 4]]

print(find_center(terminals1))
print(find_center(terminals2))


# Problem 3: Finding All Reachable Destinations
# Understand
# What is the input and output of the function?
# Is there a time or space complexity that we should be aware of?
# What should we return when the input is empty?

# Plan
# We will use a queue to keep track of the current destination and a set to keep track of visited destinations.
# Define an empty list to store the reachable destinations.
# Iterate through the queue and for each destination, check if it is connected to any other destination.
# If it is, add it to the queue and mark it as visited.
# If it is not, add it to the list of reachable destinations.
# Return the list of reachable destinations.
# time complexity is O(N + E ) where N is the number of nodes and E is the number of edges.
# space complexity is O(N).

# Implement
from collections import deque

def get_all_destinations(flights, start):
    """A function that returns all reachable destinations from a given starting point."""
    queue = deque([start])
    visited = set([start])

    reachable = []
    while queue:
        current = queue.popleft()
        reachable.append(current)

        for neighbor in flights.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return reachable


flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))