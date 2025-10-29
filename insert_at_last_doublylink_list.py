class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Create nodes
head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

# Connect nodes properly
head.next = n2
n2.prev = head
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4


def insert_at_any_pos(head, pos, data):
    new_node = Node(data)

    # If inserting at beginning
    if pos == 1:
        new_node.next = head
        head.prev = new_node
        head = new_node
        return head

    temp = head
    for i in range(1, pos - 1):
        if temp is None:
            print("Position out of range!")
            return head
        temp = temp.next

    new_node.next = temp.next
    if temp.next:
        temp.next.prev = new_node
    temp.next = new_node
    new_node.prev = temp

    return head


def display(head):
    temp = head
    while temp:
        print(temp.data, end="  ")
        temp = temp.next
    print()


head = insert_at_any_pos(head, 3, 25)
display(head)
