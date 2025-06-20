from collections import deque

# Problem 1 (Advance): Blueprint Approval Process
# Understand
# Is the given list sorted?
# Are we allowed to use built-in function?
# What the input format should like?
# Is there a time or space complexity constrain?

# Plan
# Declare a queue.
# sort the given list of blueprints, and enqueue all element in the queue.
# Define a result list.
# Iterate over the queue, dequeue element one by one, and append it to result list.
# Return result list.
# 
# Implement
def blueprint_approval(blueprints):
    """Return the order in which the blueprints are approved."""
    result = []
    my_deque = deque()
    for blueprint in sorted(blueprints):
        my_deque.append(blueprint)
    
    while my_deque:
        val = my_deque.popleft()
        result.append(val)

    return result
print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 


# Problem 2 (Advance): Build the Tallest Skyscraper
# Understand
# Is the input always sorted?
# Does the input only contain integers?
# What can we do with duplicate value?
# Is there a time or space complexity constrain?

# Plan
# Define a count variable to store the final result and a stack to keep track the current skyscrapers.
# Base cases: if len(floors) == 0, just return 0.
# If len(floors) == 1, return 1. 
# Iterate over the given floor and do the following.
# IF stack is empty, start a new skyscrapers and increment count to 1.
# If top of stack >= current floor, add next floor into stack.
# If top of stack < current floor, pop top of stack, start a new skyscraper, and increment count by 1.
# Return count. 

# Implement
def build_skyscrapers(floors):
    stack = []
    skyscrapers = 0

    for floor in floors:
        if not stack:
            stack.append(floor)
            skyscrapers += 1
        
        elif stack[-1] >= floor:
            stack.append(floor)
        
        elif stack[-1] < floor:
            while stack and stack[-1] < floor:
                stack.pop()
            stack.append(floor) 
            skyscrapers += 1
    return skyscrapers

# Example usage
print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9]))  
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

# Problem 1 (Standard): Manage Performance Stage Changes
# Understand
# Is there any time or space complexity constraint?
# What should we return when no change has occurs?

# Plan
# Declare two stacks, one to track the final result, and the second to keep track cancelled events.
# Iterate over the given performance, and check the following
# append the performance id to the stack if the change start with the word 'schedule'.
# remove the performance id from stack if the change is equal to the word 'Cancel'
# if change word is 'Reschedule', add the corresponding cancelled performance id to the stack.
# Return stack
# Implement


def manage_stage_changes(changes):
    """Function that manages performance stage"""
    stack = []
    canceled = []

    for change in changes:
        if change.startswith("Schedule"):
            performance_id = change.split()
            stack.append(performance_id[-1])
        elif change == "Cancel" and stack:
            canceled.append(stack.pop())
        elif change == "Reschedule" and canceled:
            stack.append(canceled.pop())

    return stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 