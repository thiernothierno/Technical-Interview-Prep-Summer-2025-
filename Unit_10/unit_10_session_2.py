
from collections import deque

# Problem 1: Can Rebook Flight

# Understand
# What is the input and output of the function?
# Is there a time or space complexity that we should be aware of?
# What should we return when the input is empty?

# Plan
# We will use a queue to keep track of the current destination and a set to keep track of visited destinations.
# Return True if source and destination are the same.
# Define an empty list visited to store the visited destinations.
# Inside the queue, pop the first element.
# For each neighbor of the current node,
# Check if their is a connection and if it is not visited.
# Return true if the neighbor is the destination.
# If not, add it to the queue and mark it as visited.
# If the queue is empty and we have not found the destination, return False.

# Implement


def can_rebook(flights, source, dest):
    n = len(flights)
    if source == dest:
        return True

    queue = deque([source])
    visited = [False] * n
    visited[source] = True

    while queue:
        current = queue.popleft()

        for neighbor in range(n):
            if flights[current][neighbor] == 1 and not visited[neighbor]:
                if neighbor == dest:
                    return True
                queue.append(neighbor)
                visited[neighbor] = True

    return False


flights1 = [
    [0, 1, 0],  # Flight 0
    [0, 0, 1],  # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2))


# Problem 3: Number of Flights
# Understand
# What is the input and output of the function?
# Is there a time or space complexity that we should be aware of?
# What should we return when the input is empty?

# Plan
# Define a counter variable to keep track of the number of flights.
# We will use a queue to keep track of the current destination and a set to keep track of visited destinations.
# Return True if source and destination are the same.
# Define an empty list visited to store the visited destinations.
# Inside the queue, pop the first element.
# For each neighbor of the current node,
# Check if their is a connection and if it is not visited.
# Return true if the neighbor is the destination.
# If not, add it to the queue and mark it as visited.
# If the queue is empty and we have not found the destination, return False.
# time complexity is O(N^2) where N is the number of nodes.
# space complexity is O(N).

# Implement
def counting_flights(flights, i, j):
    """Return the minimum number of flights needed to travel from airport i to airport j.
    If it is not possible to fly from airport i to airport j, return -1"""
    n = len(flights)
    if i == j:
        return 0

    queue = deque([i])
    visited = [False] * n
    visited[i] = True
    flights_count = 0

    while queue:
        flights_count += 1
        for _ in range(len(queue)):
            current = queue.popleft()

            for neighbor in range(n):
                if flights[current][neighbor] == 1 and not visited[neighbor]:
                    if neighbor == j:
                        return flights_count
                    queue.append(neighbor)
                    visited[neighbor] = True

    return -1


flights = [
    [0, 1, 1, 0, 0],  # Airport 0
    [0, 0, 1, 0, 0],  # Airport 1
    [0, 0, 0, 1, 0],  # Airport 2
    [0, 0, 0, 0, 1],  # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
