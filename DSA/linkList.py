class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
n1=Node(10)
new=Node(1220)
n2=Node(170)
n3=Node(180)
n4=Node(190)
n5=Node(180)

n1.next=new
new.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
# print(n1.data)
# print(n1.next.data)

current=n1
while current:
    print(current.data)
    current=current.next


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




# insertions



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
#insert at begining
def insert_begining(head,data):
    new_node = Node(data)
    new_node.next=head
    head=new_node
    return head
    
#insert at end    
def insert_end(head,data):
     new_node = Node(data)
     if head == None:
         return new_node
         
     current=head
     
     while current.next:
         current=current.next
     current.next=new_node
     
#display
def display(head):
    current=head
    while current.next:
         print(current.data)
         current=current.next
    print(current.data)
   
    
    
head=None
n1=Node(10)
head=n1
head=insert_begining(head,5)

insert_end(head,45)
display(head)


# print(head.data)
        
# n1=Node(10)
# new=Node(1220)
# n2=Node(170)
# n3=Node(180)
# n4=Node(190)
# n5=Node(180)

# n1.next=new
# new.next=n2
# n2.next=n3
# n3.next=n4
# n4.next=n5
# # print(n1.data)
# # print(n1.next.data)

# current=n1
# while current:
#     print(current.data)
#     current=current.next




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
                                         
def insert_position(position,data,head): 
    if position==0:                       
        return insert_begining(head,data)
    new_node=Node(data)                        
    current=head                             
    counter=0                             
                                          
    while current is not None  and counter < position -1:
        current=current.next              
        counter+=1                       
                                         
    new_node.next=current.next           
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
# display(head)
insert_position(1,70,head)
display(head)