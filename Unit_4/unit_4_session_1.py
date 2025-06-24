# Advance : Version 1

# Problem 1: Brand Filter
# Understand
# What the output format should look like?
# What shoudl we do the given brands is empty?
# What should we do when a name does not have any criterion?
# Is there a time or space complexity constrain?

# Plan
# Define an empty result list to store the output.
# Iterate over the given brands list of dictionary, and do the following:
# If criterion exist in criteria key append the name of the criterion into result list.
# Otherwise, do nothing.
# Return result list.
# Time complexity: O(n) since we need to iterate through all element present in the list. 
# Space complexity: O(n), we are declaring a list to store the names of all brands that correspond to the target criterion. 
# Implement
def filter_sustainable_brands(brands, criterion):
    """ returns a list of brands that meet the criterion."""
    result = []
    for brand in brands:
        if criterion in brand['criteria']:
            result.append(brand['name'])
    return result

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]
print("Output of Problem 1")
print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))
print("\n")

# Problem 2: Eco-Friendly Materials

# Understand
# What the output format should look like?
# What shoudl we do the given brands is empty?
# What should we do when a name does not have any criterion?
# Do we need to return material in frequency descending order?
# Is there a time or space complexity constrain?

# Plan
# Declare a dictionary to store the name and frequency of each material.
# Iterate over the given brands, and perform the following:
# Iterate over the list of material and If a material is present in dictionary, then increment it counts by 1,
# Otherwise add it with a frequency of 1. 
# Return dictionary. 
# Time complexity: O(n^2), due to the nested loop.
# Space complexity: O(n) because of the result dictionary we declare to store the output. 

# Implement
def count_material_usage(brands):
    """ takes a list of brands (each with a list of materials) and returns the material names and 
    the number of times each material appears across all brands."""
    result_distionary = {}
    for brand in brands:
        current_material = brand['materials']
        for material in current_material:
            if material not in result_distionary:
                result_distionary[material] = 1
            else:
                result_distionary[material] += 1
    return result_distionary

        
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print("Output of Problem 2")
print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))
print("\n")

# Problem 3: Fashion Trends
# Understand
# What the output format should look like?
# What shoudl we do the given brands is empty?
# What should we do when a name does not have any criterion?
# Do we need to return material in frequency descending order?
# Is there a time or space complexity constrain?

# Plan
# Declare a dictionary to store the name and frequency of each material.
# Declare an output list to store the final result.
# Iterate over the given brands, and perform the following:
# Iterate over the list of material and If a material is present in dictionary, then increment it counts by 1,
# Otherwise add it with a frequency of 1. 
# Now, Iterate over the dictionary and append the name of material with frequency greater than 1.
# Return output list.
# Time complexity: O(n^2), due to the nested loop.
# Space complexity: O(n) because of the result dictionary we declare to store the output. 
# Implement
def find_trending_materials(brands):
    """function, which takes a list of brands (each with a list of materials or practices), 
    and returns a list of materials or practices that are trending (i.e., those that appear more than once across all brands)."""
    result_distionary = {}
    output = []
    for brand in brands:
        current_material = brand['materials']
        for material in current_material:
            if material not in result_distionary:
                result_distionary[material] = 1
            else:
                result_distionary[material] += 1
    for key, value in result_distionary.items():
        if value > 1:
            output.append(key)
    return output

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print("Output of Problem 3")
print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))