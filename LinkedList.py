# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data value
        self.next = None  # Pointer to the next node (initially None)

# LinkedList class manages the linked list and its operations
class LinkedList:
    def __init__(self):
        self.head = None  # Start of the list (initially empty)

    # Function to insert a new node with 'data' at 'position'
    def insert_at_position(self, data, position):
        new_node = Node(data)  # Create a new node with the given data

        # If inserting at the beginning (position 0)
        if position == 0:
            new_node.next = self.head  # New node points to current head
            self.head = new_node       # Update head to the new node
            return

        current = self.head
        current_position = 0

        # Traverse the list to find the node just before the desired position
        while current is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        # If the position is beyond the last node, raise an error
        if current is None:
            raise IndexError("Position out of bounds")

        # Insert the new node by adjusting pointers
        new_node.next = current.next  # New node points to the next node in the list
        current.next = new_node       # Previous node points to the new node

    # Utility function to print the linked list (for verification)
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ' if current.next else '')
            current = current.next
        print()

# Example Usage
ll = LinkedList()
ll.insert_at_position(10, 0)  # Insert 10 at head, list: 10
ll.insert_at_position(20, 1)  # Insert 20 at position 1, list: 10 -> 20
ll.insert_at_position(15, 1)  # Insert 15 at position 1, list: 10 -> 15 -> 20

ll.print_list()  # Output: 10 -> 15 -> 20
