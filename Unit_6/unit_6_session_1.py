# Advance
# Problem 1: Selective DNA Deletion

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Understand
# How the output format should look like?
# What should we return when m and n are 0?
# Is there a time or space complexity constraint?

# Plan
# Define a helper function that will return the length of the linked list.
# Tacke base cases: 1- return none when the linked list is empty.
# 2- return the linked list when m is greater than the length of the original linked list.
# Assign a skip node to the head of the linked list.
# Declare two variables i and j with values 1 and 1 respectively.
# Use a while loop to skip all nodes to the size of m.
# Remove all nodes of the size of n from the linked list using a pointer called remove.
# Update skip.next to point to remove pointer.
# Make skip pointer to point to remove pointer.
# Update variables i and j to 1 and 1 respectivelly.
# Repeat the process until skip node reach to null or the end of the linked list. 
# Time complexity: O(n) since we are scaning each node in the linked list. n is the number of node in the list.
# Space complexity: O(1) as we are only declaring pointers and variables which takes no significant space. 

# Implement 
def length_of_linked_list(head):
    """Function that returns the length of a given linked list."""
    if head is None:
        return 0
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
        


def edit_dna_sequence(dna_strand, m, n):
    """Function that Retain the first m nucleotides from the current position. - Remove the next n nucleotides from the sequence."""
    if dna_strand is None:
        return None
    size = length_of_linked_list(dna_strand)
    if size < m:
        return dna_strand
    
    node_to_skip = dna_strand
    i, j = 1,1
    while node_to_skip: 
        while i < m:
            if node_to_skip is None:
                return dna_strand
            else:
                node_to_skip = node_to_skip.next
                i += 1
        
        if node_to_skip is None:
            return dna_strand
        
        node_to_remove = node_to_skip.next
        while j <= n:
            if node_to_remove is None:
                break
            else:
                node_to_remove = node_to_remove.next
                j += 1

        node_to_skip.next = node_to_remove
        node_to_skip = node_to_remove
        i = 1
        j = 1

    return dna_strand

# Review
dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

head = Node(1, Node(2, Node(3)))  
print_linked_list(edit_dna_sequence(dna_strand, 2, 3)) # Output: 
print_linked_list(edit_dna_sequence(head, 1, 1))


# Problem 2: Protein Folding Loop Detection
# Understand
# What should we do when there is no cycle?
# Do we need to return the length of the cycle or values that appears in the cycle?
# Are values in the linked list unique?
# Is there a time or space complexity constraint?

# Plan
# Declare a result empty array to store the output values.
# Declare two pointers slow and fast to check if the linked list has a cycle.
# Move slow pointer by one step, and fast pointer by two steps.
# If slow and fast pointers point to the same node, this mean there is a cycle.
# Otherwise, there is not cycle return an empty list.
# Now, we need to find the begining of the cycle, by reassigning slow pointer to the head of the linked list.
# While slow != fast, move both of them with the same speed, one step. 
# Assign another pointer to where slow and fast meet, which is the beginning of the cycle.
# Collect nodes in the cycle. 
# Return result list.


# Implement 
def cycle_length(protein):
    """Function that return all elements present in a cycle."""
    result = []
    slow = protein
    fast = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return []
       
        
    slow = protein
    while slow != fast:
        slow = slow.next
        fast = fast.next

    begining_of_cycle = slow
    while True:
        result.append(slow.value)
        slow = slow.next
        if slow == begining_of_cycle:
            break

    return result
    
# Review 
protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 
print(cycle_length(protein_head))  # Output: ['Gly', 'Leu', 'Val']

# Advance set version 2
# Problem 1: Linked List Game

# Understand
# Is it guaranteed that the linked list will contain an even nodes?
# What should we do when the linked list is none or has only one node?
# Is there a time or space complexity constraint?


# Plan
# Declare two variables even_count and odd_count to track the number of point earned by even and odd nodes. 
# Initializiae both even_count and odd_count to 0. 
# Declare a pointer current that will point to the head of the linked list.
# Start traversing the linked list from the head.
# While current is not pointing to none, do the following:
# if current.value > current.next.value, then increase the even_count variable by 1.
# Otherwise, increase the odd_count variable by 1. 
# Move current to two nodes ahead to check the next pair of node. 
# When the end is reached, if even_count > odd_count: return "Even"
# if even_count < odd_count: return "Odd", othewise, return "Tie"
# Time complexity: O(n) since we are scaning each node in the linked list. n is the number of node in the list.
# Space complexity: O(1) as we are only declaring pointer and variables which takes no significant space. 

# Implement 
def game_result(head):
    """Function that returns the name of the team with the higher points, if the points are equal, return "Tie"."""
    even_count = 0
    odd_count = 0
    current = head
    while current and current.next:
        if current.value > current.next.value:
            even_count += 1
        else:
            odd_count += 1

        current = current.next.next
    
    if even_count > odd_count:
        return "Even"
    elif even_count < odd_count:
        return "Odd"
    else:
        return "Tie"
    
game1 = Node(2, Node(1))
game2 = Node(2, Node(5, Node(4, Node(7, Node(20, Node(5))))))
game3 = Node(4, Node(5, Node(2, Node(1))))

print(game_result(game1)) # Output : Even
print(game_result(game2)) # Output : Odd
print(game_result(game3)) # Output : Tie
