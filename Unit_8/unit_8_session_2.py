# Advanced Problem Set Version 1
class TreeNode:
    def __init__(self, val, key, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right


# Understand
# What should we do when the tree is empty?
# Is is guaranteed that the given tree will be a BST?
# How the output format should be? list? tuple? 
# Do we need to take account for duplicate values?
# Is there a time or space complexity constraint?

# Plan
# Define an empty list to store the result.
# Apply inorder on the root of the tree. Which will return all nodes in sorted order.
# Recursivelly call function on left subtree.
# Append current node.key and node.val to result list.
# Recursivelly call function on right subtree.
# Return result list.

# Implement 

def sort_plants(collection):
    """Return sorted collections by key."""
    result = []
    def inorder(root):
        if not root:
            return []
        else:
            inorder(root.left)
            result.append((root.key, root.val))
            inorder(root.right)

    inorder(collection, result)
    return result

# Using build_tree() function at the top of page
# values = TreeNode((3, "Monstera"), TreeNode((1, "Pothos"), None, TreeNode((2, "Spider Plant"))),
#                   TreeNode((5, "Witchcraft orchid"), TreeNode((4, "Hoya Motoskei"))))
# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = TreeNode(values)

# print(sort_plants(collection))


# Problem 2: Flower Finding
# Understand
# What should we do when the tree is empty?
# How the output format should be? list? tuple? boolean? 
# Is there a time or space complexity constraint?
# Plan
# If not root, return False.
# Use preorder traversal to traverse the tree.
# Start from the root node, return true, if root.val equal to target.
# Recursively check the left and right subtree if target exist.

# Implement 
class TreeNode1():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    """Return True if name exist, false otherwise."""
    if not inventory:
        return False
    else:
        if inventory.val == name:
            return True
        return find_flower(inventory.left, name) or find_flower(inventory.right, name)
    
    
garden = TreeNode1("Rose", TreeNode1("Lily", TreeNode1("Daisy"), TreeNode1("Lilac")), TreeNode1("Tulip", None, TreeNode1("Violet")))
print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 


# Problem 1: Monstera Madness
# Understand
# Plan
# Implement 
def count_odd_splits(root):
    """Return total number of odd integers"""
    odd_value = 0
    def helper(node, odd_value):
        if not node:
            return 0
        else:
            value = node.val
            if value % 2 == 1:
                odd_value += node.val
            helper(node.left, odd_value)
            helper(node.right, odd_value)
        
    helper(root, 0)
    return odd_value

root = TreeNode1(2)
root.left = TreeNode1(3)
root.right = TreeNode1(6)
root.left.left = TreeNode1(6)
root.left.right = TreeNode1(7)
root.right.right = TreeNode1(12)

# values = TreeNode1(2, TreeNode1(3, TreeNode1(6), TreeNode1(7)), TreeNode1(5, None, TreeNode1(12)))
# values = [2, 3, 5, 6, 7, None, 12]
monstera = TreeNode1(root)

print(count_odd_splits(monstera))
print(count_odd_splits(None))