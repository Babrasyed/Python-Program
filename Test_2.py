# # PROGRAMMING TEST
# #               Shop Management System (Python)

# # Question Statement

# # Develop a Shop Management System using Python. The program should be menu-driven and continue running until the user chooses to exit.

# # The system should provide the following functionalities:

# # 1. Add Product
# #    - Enter Product ID, Product Name, Price, and Stock Quantity.
# #    - Store the product information in the system.

# # 2. Display Products
# #    - Display all available products with their details:
# #      • Product ID
# #      • Product Name
# #      • Price
# #      • Stock Quantity
()
# # 3. Buy Product
# #    - Ask the user to yenter a Product ID and the quantity to purchase.
# #    - Check whether the product exists.
# #    - Verify that enough stock is available.
# #    - If the purchase is successful:
# #        • Reduce the stock quantity.
# #        • Add the product to the shopping cart.
# #        • Display the total price of the purchase.

# # 4. View Cart
# #    - Display all products added to the shopping cart along with their quantities.

# # 5. Checkout
# #    - Display the final bill showing:
# #        • Product Name
# #        • Quantity Purchased
# #        • Total Price of each product
# #        • Grand Total

# # 6. Exit
# #    - Terminate the program.

# ------------------------------------------------------------------------------------------
# ========== SHOP MANAGEMENT SYSTEM ==========

# 1. Add Product
# 2. Display Products
# 3. Buy Product
# 4. View Cart
# 5. Checkout
# 6. Exit

# Enter your choice: 1

# Enter Product ID: 101
# Enter Product Name: Laptop
# Enter Price: 85000
# Enter Stock Quantity: 5

# Product added successfully.

# --------------------------------------

# Enter your choice: 2

# Product ID : 101
# Name       : Laptop
# Price      : 85000
# Stock      : 5

# --------------------------------------

# Enter your choice: 3

# Enter Product ID: 101
# Enter Quantity: 2

# Purchase successful!
# Total Cost: 170000

# --------------------------------------

# Enter your choice: 4

# Shopping Cart

# Laptop : 2

# --------------------------------------

# Enter your choice: 5

# ========== FINAL BILL ==========

# Laptop x 2 = 170000

# Grand Total = 170000

# Thank you for shopping!

# --------------------------------------

# Enter your choice: 6

# Program terminated successfully.



        





class Product:
    def __init__(self,name,pid,price,quantity):
        self.name=name
        self.pid=pid
        self.price=price
        self.quantity=quantity
        
class Shop(Product):
    def __init__(self):
        self.products=[]
    def add_product(self,prod1):
        self.products.append(prod1)
        print(self.products)
        print("Product Added")
    def display_product(self):
        for i in self.products:
             print(f"Product Name : {i.name}")
             print(f"Product ID : {i.pid}")
             print(f"Product Price : {i.price}")
             print(f"Product Quantity : {i.quantity}")
class Cart:
    def __init__(self):
        self.items=[]
    def add_item(self,product):
        self.items.append(product)
        print("Added to Cart!")
    def buy_item(self,products):
        pid=int(input("enter product id : "))
        qty=int(input("enter quantity : "))
        for p in products:
            if p.pid==pid:
                p.quantity=p.quantity-qty
                obj=Product(p.name,pid,p.price,qty)
                self.add_item(obj)
                print("purchased")
                print(f"Total cost : {p.price * qty}")
    def view_cart(self):
        for i in self.items:
            print("======Shopping Cart======")
            print(f"Product Name : {i.name}")
            print(f"Product Quantity : {i.quantity}")
    def checkout(self):
        total=0
        for i in self.items:
            total=total+(i.price*i.quantity)
        print(f"Grand Total={total}")
    
        
    
        
        
            

 
print("========== SHOP MANAGEMENT SYSTEM ==========")
print("Press 1 to Add Product")
print("Press 2 to Display Products")
print("Press 3 to Buy Products")
print("Press 4 to View Cart")
print("Press 5 to Checkout")
print("Press 6 to Eixt")
shopobj=Shop()
cartobj=Cart()
while True:
    choice=int(input("Please Enter Your Choice:"))
    if choice == 1:
        name=input("enter product name:")
        pid=int(input("enter product id:"))
        price=int(input("enter product price:"))
        quantity=int(input("enter product quantity:"))
        prod1=Product(name,pid,price,quantity)
        shopobj.add_product(prod1)
        
    elif choice == 2:
        shopobj.display_product()
    elif choice ==3:
        cartobj.buy_item(shopobj.products)
    elif choice ==4:
        cartobj.view_cart()
    elif choice ==5:
        cartobj.checkout()
        
    if choice == 6:
        print("Exit")
        break    
        
        
    



