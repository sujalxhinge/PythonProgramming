#Insert at any postion
from LinkedList import Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    #create list
head = Node(10)
second = Node(20)
third = Node(30)
head.next = second
second.next = third
#insert 30 at 3rd position
new_node = Node(40)
new_node.next = second.next
second.next = new_node
#display list
temp = head
while temp:
    print(temp.data,end="-->")
    temp = temp.next
print("NULL")


