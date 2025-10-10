class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = None
#Start with empty list
def insert_f(head,data):
     newnode = Node(data)
     newnode.next = head
     head = newnode
     return head

head = insert_f(head,30)
head = insert_f(head,20)
head = insert_f(head,10)
temp = head
while temp:
    print(temp.data, end="-->")
    temp = temp.next
print("NULL")



#

