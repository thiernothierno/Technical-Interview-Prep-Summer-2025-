# Standard Problem Set Version 1

# Problem 1: Most Endangered Species

# Understand
# What should we return when the dictionary is empty?
# What should we do when there is a tie?
# What is the format of the input? is it a list? or a dictionary?
# Is there a time or space complexity constrain?

# Plan
# Declare a variable called lowest to track the lowest population seeing so far. Initialize it to +infinity.
# Define a string variable to track the name of the specie with lowest population. Initialize it as empty.
# Iterate over the given list of species, assigne the population of the current specie to a variable called current_population.
# If current_population is lower than the lowest variable, update the lowest variable to current_population,
# And assigne the name of the current specie to the variable name_Of_specie_with_lowest_population.
# Return name_Of_specie_with_lowest_population.
# Time complexity: O(n), since we need to scan all element present in the list.
# Space complexity: O(1), no extra space used, we are only declaring variable.

# Implement
def most_endangered(species_list):
    """return the name of the species with the lowest population."""
    lowest = float('inf')
    name_of_specie_with_lowest_population = ""
    for specie in species_list:
        current_population = specie["population"]
        if current_population < lowest:
            lowest = current_population
            name_of_specie_with_lowest_population = specie["name"]
    
    return name_of_specie_with_lowest_population
            
species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 100
    }
]

# print(most_endangered(species_list))


# Problem 2: Problem 2: Identifying Endangered Species
# Understand
# What is the input format? strings? integers?
# What should we do when both or one of the parameter is empty?
# What should we do when the first parameter contain duplicate?
# Is there a time or space complexity constrain?

# Plan
# Declare a dictionary to store each character and it frequency in the observed_species.
# Declare a count variable to store the output. Initialize it to 0. 
# Use a set data structure to remove duplicate character in the endangered_species.
# For each letter in the endangered_species, if letter is present in the dictionary,
# update the count variable to the frequency of the letter.
# Return count.
# Time complexity: O(n), since we need to scan all elements.
# Space complexity: O(n), since we are using a dictionary and a set. 

# Implement
def count_endangered_species(endangered_species, observed_species):
    """count the number of endangered species observed."""
    my_dict = {}
    for char in observed_species:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1

    count = 0
    endangered_species = set(endangered_species)
    for c in endangered_species:
        if c in my_dict:
            count += my_dict[c]
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  


# Standard Problem Set Version 2
# Problem 1: Filter Destinations

# Understand
# Does the rating_scores always represented as an integer?
# What should we do when a City has not a rating score?
# What the output format would be? list, dictionary?
# Is there a time or space complexity constrain?

# Plan
# Use list comprehension to replicate the original dictionary.
# Iterate over the new list and remove all rating below the rating_threshold.
# Return the new list.
# Time complexity: O(n), since we need to scan all value in the dictionary.
# Space complexity: O(n), since we are using a dictionry to replicate the original dictionary.

# Implement

def remove_low_rated_destinations(destinations, rating_threshold):
    """Function that returns the updated dictionary after removing all rating below the given threshold."""
    new_list = {key: value for key, value in destinations.items()
                if value > rating_threshold}
    return new_list


destinations1 = {"Paris": 4.8, "Berlin": 3.5,
                 "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9,
                 "Tokyo": 4.5, "Sydney": 3.0}

print(remove_low_rated_destinations(destinations1, 4.0))
print(remove_low_rated_destinations(destinations2, 4.9))