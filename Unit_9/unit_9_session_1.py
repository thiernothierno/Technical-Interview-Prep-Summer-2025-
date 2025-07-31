
from collections import deque

class TreeNode():
    def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Problem 1: Merging Cookie Orders
# Understand
# What should we do return when both trees are null or one of them is null?
# Is both tree has the same height?
# Is the merge be done by level?
# Are we building a new tree as a result of the merge?
# Is their a time or space complexity constraint?

# Plan
# Check for base cases: 1- Return None when both trees are nulls.
# 2- Return tree1 if tree2 is null, or tree2 if tree1 is null.
# Define a helper function to do the work. 
# Start traversal from both roots.
# Define a variable sum_val to store the current sum.
# Create a new node merge_node and add sum_Val as it value.
# Recursivelly call the helper function on the left of both trees and assign it to merge_node.left.
# Recursivelly call the helper function on the right of both trees and assign it to merge_node.right.
# Return merge_node.
# Inside the main function, return the helper function and pass both roots as parameters.

# Implementation
def merge_orders(order1, order2):
    """Return a merge tree."""
    def helper(root_1, root_2):
        if root_1 is None and root_2 is None:
            return None
        if not root_1:
            return root_2
        if not root_2: 
            return root_1
        sum_val = 0
        sum_val = root_1.val + root_2.val
        merge_nodes = TreeNode(sum_val)
        merge_nodes.left = helper(root_1.left, root_2.left)
        merge_nodes.right = helper(root_1.right, root_2.right)
        return merge_nodes

    return helper(order1, order2)

        
root_1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
root_2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
print("\nOutput Problem 1: ")
print_tree(merge_orders(root_1, root_2))
    


# Problem 3: Maximum Tiers in Cake
# Understand
# What should we do return when the root is None?
# Are we returning the longest path of the tree?
# Is there a time a space complexity constraint?

# Plan
# Define a helper function to do the magic work.
# Check for base case: Return 0 if root is None.
# Start traversal from the root node.
# Recursively find the height of the left subtree and assign it value to a variable call left_Val.
# Recursively find the height of the right subtree and assign it value to a variable call right_Val.
# Return max(left_val, right_val) + 1. We add 1 for the root node.
# Time Complexity: O(h), where h is the height of the tree.
# Space complexity: O(n), due to the recursive calls.

# Implementation
def max_tiers(cake):
    """Return height of the tree."""
    def helper(root):
        if root is None:
            return 0
        left_val = helper(root.left)
        right_val = helper(root.right)
        return max(left_val, right_val) + 1
    return helper(cake)

root = TreeNode("Chocolate", TreeNode("Vanilla"), TreeNode("Strawberry", TreeNode("Chocolate"), TreeNode("Coffee")))
print("\nOutput Problem 2: ")
print(max_tiers(root))

# Advance problem

# Problem 1: Croquembouche II

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
# Define another empty list called result that will store nodes by leve.
# Iterate over the range of n.
# Pop all elements in queue and append them to result list.
# Add both left and right childs of current node to queue if they exist.
# Outside the iteration, append result list to output list.
# Return output list at the end.
# Time complexity: O(h), where h is the height of the tree.
# Space complexity: O(n), due to the two lists we have declared. 

# Implementation
def listify_design(design):
    """return a list of lists of nodes by level"""
    output = []
    queue = deque([design])
    while queue:
        n = len(queue)
        result = []
        for _ in range(n):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            result.append(node.val)
        output.append(result)
    return output

croquembouche = TreeNode("Vanilla", 
                    TreeNode("Chocolate", TreeNode("Vanilla"), TreeNode("Matcha")), 
                    TreeNode("Strawberry"))
print("\nOutput Problem 3: ")
print(listify_design(croquembouche))