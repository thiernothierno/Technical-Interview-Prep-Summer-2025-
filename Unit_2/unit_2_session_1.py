# Advance Problem 

# Problem 1: Counting Treasure

# Understand
# Is there a time or space complexity constrain?
# What should we return when the dictionary is empty?

# Plan
# Declare a variable result to store the total number of treasures buried.
# Iterate over the dictionary and add all the value of each key to the variable result.
# Return the variable result.
# Time complexity: O(n), since we need to go through all values in the dictionary.
# Space complexity: O(1), no extra space used. 
# Implement
def total_treasures(treasure_map):
    """ returns the total number of treasures buried on the island."""
    result = 0
    for key, value in treasure_map.items():
        result += value
    return result

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2)) 

# Problem 2: Pirate Message Check
# Understand
# Does the message contain any other character beside alphabetic letter or space?
# Are we allowed to use built-in functions?
# Is there a time or space complexity constrain?

# Plan
# Remove all space(s) from the given string.
# Remove all duplicate letters from the given string using the built-in set data structure.
# Return True if the length of the remaining letters is equal to 26, otherwise false.
# Time complexity: O(1) since we are only performing a check operation on the length of the string. 
# Space complexity: O(n) since we are using an extra space to store all unique letters. 

# Implement
def can_trust_message(message):
    """Returns True if the message contains every letter of the English alphabet at least once, and False otherwise"""
    new_message = message.replace(" ", "")
    new_message = set(new_message)
    if len(new_message) == 26:
        return True
    return False

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))

# Problem 3: Find All Duplicate Treasure Chests in an Array
# Understand
# Is the array sorted?
# Is there a time or space complexity constrain?
# What should we do when the array is empty or contain only one element?
# Can we return the output in any order?

# Plan
# Declare an empty result list to store the final output.
# Use a dictionary to store all element in the array as a key-value pair format. Where keys are interger values present in the array,
# and their value correspond to the frequency of each integer.
# Iterate over the array, if element already in dictionary increment it frequency by 1, otherwise add it to the dictionary with a frequency of 1.
# Iterate over the dictionary, and append all keys with frequency equal to 2 to the result list.
# Return result list.
# Time complexity: O(n) since we need to scan all elements in the array.
# Space complexity: o(n) as we are using extra space to store elements in a dictionary, and to store the final result. 

# Implement
def find_duplicate_chests(chests):
    """Return an array of all the integers that appear twice, representing the treasure chests that have duplicates."""
    result = []
    my_dictionary = {}
    for val in chests:
        if val in my_dictionary:
            my_dictionary[val] += 1
        else:
            my_dictionary[val] = 1
    

    for key, val in my_dictionary.items():
        if val == 2:
            result.append(key)
    return result
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))