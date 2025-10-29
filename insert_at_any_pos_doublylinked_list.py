class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

head.next = n2
n2.next = n3
n2.prev = head
n3.next = n4
n3.prev = n2
n4.next = n5
n5.prev = n3
n5.prev = n4

def insert_at_any_pos(head,pos,data):
    new_node = Node(data)
    temp = head
    count = 1
    while count < pos-1:
        temp = temp.next
        count += 1
    new_node.next = temp.next
    new_node.prev = temp
    temp.next.prev = new_node
    temp.next = new_node
    return head

def display(head):
    temp = head
    while temp:
        print(temp.data, end="  ")
        temp = temp.next

insert_at_any_pos(head,3,25)
display(head)
