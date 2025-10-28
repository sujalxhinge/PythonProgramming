class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
#inititalize head as NULL
head = None
#function to insert node at first postion
def insert_at_beginning(data):
    global head
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        new_node.next = head
        head.prev = new_node
        head = new_node

#function to display the doubly linked list
def display():
    temp = head
    while temp:
        print(temp.data, end=" --> ")
        temp = temp.next
    print("Null")
insert_at_beginning(5)
insert_at_beginning(6)
insert_at_beginning(7)
display()




