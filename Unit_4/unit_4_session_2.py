# Advance 
from collections import deque

# Problem 1: Count Unique Characters in a Script
# Understand
# Is the key in the script always a strings?
# What should we do when the dictionary is empty?
# Is there a time or space complexity constrain?

# Plan
# Use a set to remove duplicate element.
# Iterate over all keys present in the dictionary.
# append them to the set.
# Return the length of the set.
# Time complexity: O(n) since we need to scan all keys in the dictionary.
# Space complexity: O(n) as we need a set to store unique element.

# Implement
def count_unique_characters(script):
    """count the number of unique characters in the script."""
    result = set()
    for name in script.keys():
        result.add(name)
    return len(result)


script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"]
}
print(count_unique_characters(script)) 

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"]
}
print(count_unique_characters(script_with_redundant_keys)) 


# Problem 2: Find Most Frequent Keywords
# Understand
# What should we do when there is a duplicate?
# What should we do when the scenes is empty or has only one element?
# Is there a time or space complexity constrain?

# Plan
# Define a dictionary to store all elements from the scene and their frequency.
# Declare a result list to store the final result.
# Iterate of the scenes and add all elements in the dictionary as well their correspondant frequency.
# Find the maximum value in the dictionary.
# Append all keys in the dictionary that have value equal to maximum value.
# Return result list.
# Time complexity: O(n) since we need to scan all keys in the dictionary.
# Space complexity: O(n) because we are using a dictionary, and a list to store the final result. 

# Implement

def find_most_frequent_keywords(scenes):
    """Return the keyword that appears the most frequently across all scenes. 
    If there is a tie, return all the keywords with the highest frequency."""
    my_dictionary = {}
    result = []
    for value in scenes.values():
        for name in value:
            if name in my_dictionary:
                my_dictionary[name] += 1
            else:
                my_dictionary[name] = 1
    max_val = float('-inf')
    for val in my_dictionary.values():
        if val > max_val:
            max_val = val
    for key, val in my_dictionary.items():
        if val == max_val:
            result.append(key)
    
    return result



scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"]
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"]
}
print(find_most_frequent_keywords(scenes)) 


# Problem 3: Track Scene Transitions

# Understand
# What should we do when the list is empty?
# What is the format of the final result?
# Is there a time or space constrain? 

# Plan
# Intialize a queue.
# Append all elements of the list in the queue.
# Iterate over the queue, remove, and access the first and second element in the queue respectively.
# Display the result of each iteration.
# Time complexity: O(n) since we need to scan all element in the list.
# Space complexity: O(n) as we need a queue to store element from the list.

# Implement 
def track_scene_transitions(scenes):
    """Function that keep track of the transitions from one scene to the next"""
    queue = deque()
    for scene in scenes:
        queue.append(scene)
    while len(queue) > 1:
        current = queue.popleft()
        next = queue[0]
        print(f"Transition from {current} to {next}.")


scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)

scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)