# Advance 
# Set Version 1

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Understand
# Plan
# Implement 
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        """Function that return True if queue is empty, false otherwise."""
        # return none when there is not element in front. 
        if not self.front:
             return None


    def enqueue(self, song, artist):
        """Function that adds tuple to the end of queue."""
        # Create a new node
        new_node = Node(song, artist)
        # enqueue node from the rear when there is no node in queue.
        if not self.rear:
             self.rear = new_node
        self.rear.next = new_node
        # assign front to new_node when there is no node in the front. 
        if not self.front:
             self.front = new_node
        
             
    
    def dequeue(self):
        """Function that removes the front element in a queue."""
        # return none when the queue is empty.
        if self.is_empty():
             return None
        # define a variable to point the front node of the queue.
        node = self.front
        self.front = self.front.next
        if not self.front:
             self.rear = None
        # remove node from the queue
        return node.value
             
    
    def peek(self):
        """Function that return the front element in a queue without removing it."""
        # Return none when the queue is empty.
        if self.is_empty():
             return None
        # Define a variable pointing to the first element in queue
        # Display the value of the variable.
        node = self.front
        return node.value

# Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue('Love Song', 'Sara Bareilles')
q.enqueue('Ballad of Big Nothing', 'Elliot Smith')
q.enqueue('Hug from a Dinosaur', 'Torres')
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty())

# Problem 2: Merge Playlists
# Understand
# Is a and b always positif? 
# Is b alwyas greater than a? What should we do when the value of a > b?
# What about if a and b both equal to 0? 
# What should we do when a and b are greater than the length of the first linked list?
# The length of first playlist always greater than or equal to b?

# Plan
# Find the length of the first linked list and assign it value to a variable called size.
# Start checking for edge cases.
# 1- if a > b > size, return the first linked list.
# Declare two pointers v and w, initially pointing to the head of the first linked list.
# Move pointer v to the length of a.
# Move pointer w to the length of b. 
# Declare two other pointers x and y and make them point the head and tail of the second linked list respectivelly.
# Traverse the first linked list, and update link with the following:
# v.next = x
# y.next = w.next
# return head of first linked list.

# Implement 

def merge_playlists(playlist1, playlist2, a, b):
    """Remove playlist1's nodes from the ath to the bth node and put playlist2 in its place"""
    v = playlist1
    w = playlist1
    for i in range(a-1):
         v = v.next
    for j in range(b):
         w = w.next
    
    # make third pointer pointing the head of second linked list.
    x = playlist2
    # Move fourth pointer to the tail of second linked list.
    y = playlist2
    while y.next:
         y = y.next

    # Update links
    v.next = x
    y.next = w.next

    # Return head of first linked list.
    return playlist1


playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

# print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))



# Problem 3: Shuffle Playlist
# Understand
# Is the length of the linked list always even?
# What should we do when the length of the linked list is odd?


# Plan
# Find the middle elment of the linked list using the slow and fast pointer approach.
# Reverse the second half of the linked list.
# Split the linked list into halves.
# Merger the two halves
# Return the head node

# Implement 
def shuffle_playlist(playlist):
    """Function that Shuffle a linked list"""
    if not playlist or not playlist.next:
        return playlist
    
    # Step 1: Find the middle of the list
    slow, fast = playlist, playlist
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half
    prev, curr = None, slow.next
    slow.next = None  # Split the list into two halves
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # Step 3: Merge the two halves
    first, second = playlist, prev
    while second:
        next_first, next_second = first.next, second.next
        first.next = second
        second.next = next_first
        first = next_first
        second = next_second
    
    return playlist

    
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
# print_linked_list(shuffle_playlist(head))



