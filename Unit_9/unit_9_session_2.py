import math
from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
# Problem 1: Balanced Baked Goods Display

# Understand
# What does it mean for a tree to be balanced?
# Does an empty tree considered balanced?
# Is there a time or space complexity constraint?

# Plan
# Define a helper function that will return the check of a tree.
# Return True if root is None.
# Find the check of left subtree and assign it value to a variable called left_val.
# Find the check of right subtree and assign it value to a variable called right_val.
# Return True if the absolute difference of left_val and right_val is greater than 1 and all subtrees from left and right are also balance.
# Otherwise, return False

# Implementation
def is_balanced(display):
    """Return True if a given tree is balanced, false otherwise."""
    def check(root):
        if root is None:
            return (0, True)
        
        left_height, left_balanced = check(root.left)
        right_height, right_balanced = check(root.right)
        current_height = max(left_height , right_height) + 1
        is_current_balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced

        return (current_height, is_current_balanced)
    
    height, balanced = check(display)
    return balanced

baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
display1 = build_tree(baked_goods)
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)

print("\nOutput Problem 1: ")
print(is_balanced(display1)) 
print(is_balanced(display2))  


# Problem 2: Sum of Cookies Sold Each Day
# What should we return when the root is None?
# Are we returning nodes level wise?
# Is there a time or space complexity constraint?

# Plan
# Check for base case: return an empty list when root is None.
# Have a deque to store nodes by level.
# Define an empty list to store the final output.
# Declare a queue to store the root node. 
# While queue is not empty:
# Assign the length of the queue to a variable n. 
# Define a variable curr_sum that will store the sum of nodes by level.
# Iterate over the range of n.
# Pop all elements in queue and add them to curr_sum.
# Add both left and right childs of current node to queue if they exist.
# Outside the iteration, append curr_sum to output list.
# Return output list at the end.
# Time complexity: O(h), where h is the height of the tree.
# Space complexity: O(n), due to the two lists we have declared. 

# Implementation
def sum_each_days_orders(orders):
    """return a list of the sums of all cookies ordered in each day (level) of the tree."""
    output = []
    queue = deque([orders])
    while queue:
        n = len(queue)
        curr_sum = 0
        for _ in range(n):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            curr_sum += node.val
        output.append(curr_sum)
    return output

order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)
print("\nOutput Problem 2: ")
print(sum_each_days_orders(orders))


# Problem 3: Sweetness Difference
# Understand
# What should we return when the root is None?
# Are we returning nodes level wise?
# Is there a time or space complexity constraint?

# Plan
# Check for base case: return an empty list when root is None.
# Have a deque to store nodes by level.
# Define an empty list to store the final output.
# Declare a queue to store the root node. 
# While queue is not empty:
# Assign the length of the queue to a variable n. 
# Declare an empty list curr_list to store all nodes present in cureent level.
# Iterate over the range of n.
# Pop node one by one from queue.
# Add both left and right childs of current node to queue if they exist.
# Outside the iteration, 
# Find min and max value of current level and assign their value to variables min_val, max_val respectivelly.
# Define a variable curr_diff to store the absolute difference between min_val and max_val.
# append curr_diff to output list.
# Return output list at the end.
# Time complexity: O(h), where h is the height of the tree.
# Space complexity: O(n), due to the two lists we have declared. 
# Plan
# Implementation
def sweet_difference(chocolates):
    """Returns a list of the absolute differences between the highest and lowest sweetness levels in each row of the chocolate box."""
    output = []
    queue = deque([chocolates])
    while queue:
        n = len(queue)
        curr_list = []
        for _ in range(n):
            node = queue.popleft()
            curr_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        min_val = min(curr_list)
        max_val = max(curr_list)
        abs_diff = (max_val - min_val)
        output.append(abs_diff)
    return output

sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels1)

sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels2)


print("\nOutput Problem 3 ")

print(sweet_difference(chocolate_box1))  
print(sweet_difference(chocolate_box2)) 