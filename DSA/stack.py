class Stack:
        def __init__(self):
            self.items=[]
    #push element to stack
        def push(self,item):
            self.items.append(item)
            print(f"Item {item} pushed to stack")

    #pop element from stack 
        def pop(self):
            if self.items==[]:
                print("stack is empty")
            else:
                removed_item=self.items.pop()
                print(f"{removed_item} popped from stack")
            
    #view the top element
        def peek(self):
            if self.items==[]:
             print("stack is empty")
            else:
                print(f"Top element : {self.items[-1]}")
            
        def display(self):
            print("Stack (Top --> bottom)")

        if self.items==[]:
            print("stack is empty")
        else:
            print("\n      Top")
            print("      ---")
            for i in reversed(self.items):
                print(f"     | {i} |")
                print("      ---")
          
            
stackObj=Stack()
stackObj.push(3)
stackObj.push(4)
stackObj.push(9)
stackObj.push(4)
stackObj.display()
stackObj.peek()
stackObj.pop()
stackObj.peek()
stackObj.display()