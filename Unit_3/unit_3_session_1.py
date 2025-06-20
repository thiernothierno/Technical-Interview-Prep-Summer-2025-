
# Problem 1 (Advance): Reveal Attendee List in Order
# Understand
# Is the given list sorted?
# Does the input only contains "I" and "D" letters?
# Is there a time or space complexity constrain?
# What should we do when the input is empty or has only one element?

# Plan
# Declare a stack and an empty list to store the final result.
# Iterate over the given list.
# Append the current index into stack.
# If the current index is equal to "I" or all elements have bein scanned, then while the stack is not empty, pop the top of stack and append it to the list result.
# return the result list after joining all it elements.

# Implement 
def arrange_guest_arrival_order(arrival_pattern):
    """Return the lexicographically smallest possible string guest_order that meets the conditions"""
    stack = []
    result = []
    for i in range(len(arrival_pattern) + 1):
        stack.append(str(i+1))
        if i == len(arrival_pattern) or arrival_pattern[i] == "I":
            while stack:
                top_element = stack.pop()
                result.append(top_element)
    return "".join(result)

# print(arrange_guest_arrival_order("IIIDIDDD"))  
# print(arrange_guest_arrival_order("DDD")) 


# Problem 2 (Advance): Problem 2: Reveal Attendee List in Order
# Understand
# Does the input contain duplicates?
# Does the input hold only integer values?
# Is there a time or space complexity constrain?


# Plan
# Start with an empty deque (double-ended queue).
# For each number in sorted_attendees from largest to smallest:
# If the deque is not empty:
# Pop the last element and insert it at the front (this reverses the "move to bottom" step).
# Insert the current number at the front.
# When finished, the deque holds the correct initial arrangement.

# Implement 
from collections import deque

def reveal_attendee_list_in_order(attendees):
    """Return an ordering of the registration numbers that would reveal the attendees in increasing order."""
    my_deque = deque(range(len(attendees)))
    result = [0] * len(attendees)
    for attendee in sorted(attendees):
        result[my_deque.popleft()] = attendee
        if my_deque:
            my_deque.append(my_deque.popleft())
        

    return result

# print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
# print(reveal_attendee_list_in_order([1,1000]))




# Problem 1 (Standard): Post Format Validator

# Understand
# What should we return when the string is emplty?
# Is there any time or space complexity constraint?
# Is it guaranteed that the string will containt only tags:  '()', '[]', '{}'?

# Plan
# Declare an emplty stack.
# Iterate over the string and check the following:
# If it is an opening tag added it to the stack
# If it is a closing tag and current stack not empty, check if their is a match
# If their is a match with top element in stack, pop top element from stack.
# Otherwise, return false.
# If stack is empty, return True
# Otherwise, return False

# Implement
def is_valid_post_format(posts):
    """Function that checks corresponding tags of the same type"""
    stack = []
    tags = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    opening_tags = '(,[,{'
    closing_tags = '), ], }'
    for tag in posts:
        if tag in opening_tags:
            stack.append(tag)
        elif tag in closing_tags:
            if not stack or stack.pop() != tags[tag]:
                return False

    return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))