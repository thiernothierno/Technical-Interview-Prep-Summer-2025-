# ADVANCE PROBLEMS

# Problem 1: Hunny Hunt
# Understand
# What should we do when the list is empty?
# What type of element does the list contain(strings, integers, floats)?
# Does the list contain duplicates?
# Is there a time or space complexity constraint?
# What should we do when there is no match?

# Plan
# Iterate over the given list and start comparaison.
# if element at current index matches with the target value, return index.
# return -1, when their is no match found.
# Time Complexity: O(1) if match found at first index. Worse case time complexity is O(n). 
# Space Complexity : O(1), no space used.

# Implement
def linear_search(lst, target):
    """return the first index of target in items, and -1 if target is not in the lst"""
    n = len(lst)
    for i in range(n):
        if lst[i] == target:
            return i
    return -1

# Review
items_1 = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target_1 = 'hunny'
# print(linear_search(items_1, target_1))

items_2 = ['bed', 'blue jacket', 'red shirt', 'hunny']
target_2 = 'red balloon'
# print(linear_search(items_2, target_2))


# Problem 2:  Bouncy, Flouncy, Trouncy, Pouncy
# Understand
# What should we do when we encounter an element inside the list operations that is not part of the given constraint operations?
# Is there a time or space complexity constraint?

# Plan
# Define a variable tigger and set it to 1.
# Iterate over the operations list and do the following:
# Increment the value of tigger if item in operation equal to 'bouncy' or 'flouncy'.
# Otherwise, decreament the value of tigger by -1.
# return tigger.
# Time Complexity: O(1) if match found at first index. Worse case time complexity is O(n). 
# Space Complexity : O(1), no space used.

# Implement
def final_value_after_operations(operations):
    """return the final value of tigger after performing all the operations"""
    tigger = 1
    for item in operations:
        if item == "bouncy" or item == "flouncy":
            tigger += 1
        elif item == "trouncy" or item == "pouncy":
            tigger -= 1
    return tigger

# Review
operations_1 = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations_1))

operations_2 = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations_2))



# Problem 3:  T-I-Double Guh-Er II
# Understand
# What should we return when the given word does not contain the target substrings?
# Is there a time or space complexity constraint?
# 
# Plan
# Store all target substrings into a list called target_substring.
# Conver given word into a lowercase.
# Formula to find all substrings of a given word: n(n+1) / 2, where n is the length of the word.
# Iterate over the new word.
# replace all substrings present in target_substring with an empty space.
# return new_word.
# Time Complexity: O(n) since we have to scan all substrings. 
# Space Complexity : O(1), no space used.

# Implement
def tiggerfy(word):
    """ returns a new string that removes any substrings t, i, gg, and er from word"""
    target_substring = ['t', 'i', 'gg', 'er']
    new_word = word.lower()
    
    for val in target_substring:
        new_word = new_word.replace(val, "")
    return new_word


# Review
word_1 = "Trigger"
# print(tiggerfy(word_1))

word_2 = "eggplant"
# print(tiggerfy(word_2))

word_3 = "Choir"
# print(tiggerfy(word_3))

