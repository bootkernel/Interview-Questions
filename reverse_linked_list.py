# Creating a class called Node
class Node:
   # Constructor and self
   def __init__(self, data, next_node=None):
      self.data = data
      self.next_node = next_node

# Reverse Linked List Function
def reverse_linked_list(starting_head_node):
   current_node = starting_head_node         # We will always start with the starting_head_node
                                             # and set the starting_head_node node as current

   previous_node = None                      # Previous node is set to null

   while current_node is not None:           # While the current_node is not
                                             # null keep looping

      next_node = current_node.next_node     # Assign the next_node to the
                                             # next_node of the current_node

      current_node.next_node = previous_node # Assign the next_node of the
                                             # current_node to the previous_node

      previous_node = current_node           # Assign the previous_node to
                                             # the current_node

      current_node = next_node               # Assign the current_node to the
                                             # next_node

   return previous_node                      # Returning previous_node

# Printing the Linked List
def linked_list(starting_head_node):
   structure = "" # Blank
   current_node = starting_head_node
   # Using loop to print the list
   while current_node:
      structure = structure + str(current_node.data) + " --> "
      current_node = current_node.next_node
   print(structure)

# Testing Data
print("\nGiven Linked List:")
starting_head_node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
linked_list(starting_head_node)
print("\nReversed Linked List:")
rev = reverse_linked_list(starting_head_node)
linked_list(rev)

# Output
# Given Linked List:
# 1 --> 2 --> 3 --> 4 --> 5 --> 

# Reversed Linked List:
# 5 --> 4 --> 3 --> 2 --> 1 --> 
