# Advance Problem

# Problem 1: Transpose Matrix
# Understand
# What should we do with empty matrices?
# Is it guaranteed that the matrix is always square?
# Is there a time or space complexity constraint?

# Plan
# Find number of rows and columns of the original matrix.
# Define a result matrix with the same size as the original matrix.
# Use a nested loop and assign result[j][i] = matrix[i][j]
# Return result matrix.
# Time complexity: o(row * col) since we are using a nested loop.
# Space complexity: o(row * col ), as we are declaring a matrix with same size as original. 

# Implement
def transpose(matrix):
    """Return the transpose matrix"""
    row = len(matrix)
    col = len(matrix[0])
    result = [[0 for _ in range(row)] for _ in range(col)]
    print(result)

    for i in range(row):
        for j in range(col):
                result[j][i] = matrix[i][j]
                
    return result

# matrix_1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(transpose(matrix_1))

# matrix_2 = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(transpose(matrix_2))


# Problem 2: Two-Pointer Reverse List
# Understand
# What should we do when the list is empty or contain only one element?
# Is there a time or space complexity constrain?
# Are we allowed to use python built-in function?

# Plan
# Declare two pointers low and high with respective value 0 and len(lst) - 1
# Swape element in the list while low < high
# update low to low + 1 and high to high - 1
# Return list.
# Time Complexity: O(n/2) since we are traversing only half of the list.  
# Space Complexity : O(1), no space used.

# Implement
def reverse_list(lst):
    """Return the list in reverse order."""
    low = 0
    high = len(lst) -1
    while low < high:
        tmp = lst[low]
        lst[low] = lst[high]
        lst[high] = tmp
        low += 1
        high -= 1
    return lst

# Review
# lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# print(reverse_list(lst))



# Problem 3: Remove Duplicates

# Understand
# Is the give list always sorted?
# Is there a time or space complexity constraint?
# Are we allowed to use built-in function?

# Plan
# Declare two pointers i and j that point respectively index 0 and 1 of the given list.
# While j is less than the length of the given list, do the following:
# if lst[i] == lst[j], increment the value of j by 1.
# otherwise, replace the value at index i + 1 with value at index j and increment both i, and j by 1.
# Return all element from 0 to i+1 position. 
# Time complexity : O(n) since we need to traverse all element of the list.
# Space Complexity: O(1), no space used.

# Implement
def remove_dupes(items):
    """Return list of items without duplicate"""
    i, j = 0, 1
    while j < len(items):
        if items[i] == items[j]:
            j += 1
        else:
            items[i+1] = items[j]
            i += 1
            j += 1
    result = items[:i+1]
    return len(result)

# items_1 = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
# print(remove_dupes(items_1))

# items_2 = ["extract of malt", "haycorns", "honey", "thistle"]
# print(remove_dupes(items_2))


# Problem 4: Sort Array by Parity

def sort_by_parity(nums):
    """Return sorted array by parity."""
    # Base case when the list has only one element. 
    if len(nums) == 1:
        return nums
    # Define empty even and odd list
    evens = []
    odds = []
    # Iterate over nums and append all even numbers into even list and odd numbers into odd list.
    for val in nums:
        if val % 2 == 0:
            evens.append(val)
        else:
            odds.append(val)
    # Append all odd values from the odd list into the even list.
    for odd in odds:
        evens.append(odd)
    # Return even list.
    return evens

# Evaluate
# Time complexity : 0(n)
# Space complexity: O(n), follow up question: can we solve this problem with a constant space complexity : O(1)?


# Improving Space Complexity:
def sort_by_parity_with_constant_space(nums):
    # Base case 
    if len(nums) == 1:
        return nums
    # Define a variable i and initialize it to zero.
    i = 0
    # Iterate over nums 
    for j in range(len(nums)):
        if nums[j] % 2 == 0:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
    return nums

nums = [3,1,5,8,10]
print(sort_by_parity_with_constant_space(nums))
