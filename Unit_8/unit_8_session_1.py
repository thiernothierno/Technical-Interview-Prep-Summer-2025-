# Advanced Problem Set Version 1


# Problem 1: Ivy Cutting
# Understand
# What should we do when the tree is empty?
# How about when the root node has no child?
# How the output format should be? list? tuple? 
# Do we need to take account for duplicate values?
# Is there a time or space complexity constraint?

# Plan
# Define an empty list output to store the result, initially empty.
# Start the iteration from the root node.
# If root node doesn't exist, return output list.
# If root node append the value of it to the list.
# Recursivelly make a call on the right node.
# Extend the result list to our output list.
# Return output list.
# Time complexity: O(n), due to the height of the tree.
# Space complexity: O(n), due to the call stack.
# Implement 
class TreeNode:
    """Class tree"""
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    """Return all rightmost node of the tree."""
    if not root:
        return []
    output = [root.val]
    right_path = right_vine(root.right)
    output.extend(right_path)
    
    return output
        
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print("\nOutput of Problem 1: ")
print(right_vine(ivy1))
print(right_vine(ivy2))


# Problem 2: Ivy Cutting II
# Understand
# What should we do when the tree is empty?
# How about when the root node has no child?
# How the output format should be? list? tuple? 
# Do we need to take account for duplicate values?
# Is there a time or space complexity constraint?

# Plan
# Define an empty list to store the result.
# If the tree is empty, return the empty list.
# Declare a variable curr to point the root node.
# Iterate over the tree.
# Append the value of current node.
# If node.right exist, point curr to the right node
# Otherwise, break the loop
# Return list.
# Time complexity: O(n), due to the height of the tree.
# Space complexity: O(n), due to the result list.
# Implement 
def right_vine_iteratively(root):
    """Return all right nodes from root node iteratively."""
    if not root:
        return []
    result = []
    curr = root
    while curr:
        result.append(curr.val)
        if curr.right:
            curr = curr.right
        else:
            break
    return result

ivy3 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy4 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print("\nOutput of Problem 2: ")
print(right_vine_iteratively(ivy1))
print(right_vine_iteratively(ivy2))


# Problem 3: Pruning Plans
# Understand
# What should we do when the tree is empty?
# How about when the root node has no child?
# How the output format should be? list? tuple? 
# Do we need to take account for duplicate values?
# Is there a time or space complexity constraint?

# Plan
# Declare an result list to store the output values, initially empty.
# Define a helper function.
# Inside helper function, if return [] if root is none.
# Recursivelly call the helper function on the left subtree.
# Recursivelly call the helper function on the right subtree.
# Append the value of current node to result list.
# Inside main function
# Call helper function passing root and result list as parameters.
# Return result list.

# Implement
def survey_tree(root):
    """Return nodes in postorder.""" 
    result = []
    def helper(node):
        if not node:
            return []
        else:
            helper(node.left)
            helper(node.right)
            result.append(node.val)

    helper(root)
    
    return result
    
magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print("\nOutput of Problem 3: ")
print(survey_tree(magnolia))