#linklist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
new=Node(46)      
n1=Node(21)

n2=Node(32)
n3=Node(75)
n4=Node(54)
n5=Node(60) 
new2=Node(9)

new.next=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=new2


print(n1.data)

# Linklist Practice

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_begining(head,data):
    new_node=Node(data)
    new_node.next=head
    head=new_node
    return head
def insert_end(head,data):
    new_node=Node(data)
    current=head
    while current.next:
        current=current.next
    current.next=new_node
def display(head):
    current=head
    while current.next:
        print(current.data)
        current=current.next
    print(current.data)  

head=None
n1=Node(50)
head=n1
head=insert_begining(head,40)
insert_end(head,90)
display(head)




        
        
        
    































