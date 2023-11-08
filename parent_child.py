#!/usr/bin/env python
# coding: utf-8

# In[3]:


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, discount):
        self.products[product_id] = {"name": product_name, "discount": discount}

    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id):
        if product_id in self.available_products:
            self.cart.append(self.available_products[product_id])
            print(f"Product added to cart: {self.available_products[product_id]['name']}")
        else:
            print("Product not found.")

    def view_cart(self):
        print("Products in your cart:")
        for product in self.cart:
            print(f"Product Name: {product['name']}")

    def generate_bill(self):
        total_price = 0
        print("Your Bill:")
        for product in self.cart:
            print(f"Product Name: {product['name']}, Discount: {product['discount']}%")
            total_price += 100 - product['discount']
        print(f"Total Price: ${total_price}")


def main():
    admin = Admin("admin", "adminpass")
    admin.add_product(1, "Product1", 10)
    admin.add_product(2, "Product2", 5)

    buyer = Buyer("buyer", "buypass", admin.products)

    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_username = input("Admin Username: ")
            admin_password = input("Admin Password: ")
            if admin_username == admin.username and admin_password == admin.password:
                while True:
                    action = input("Add or subtract a product (a/s), or quit (q): ").lower()
                    if action == 'a':
                        num_products = int(input("How many products do you want to add: "))
                        for _ in range(num_products):
                            product_id = int(input("Product ID: "))
                            product_name = input("Product Name: ")
                            discount = int(input("Discount on the product (%): "))
                            admin.add_product(product_id, product_name, discount)
                            print(f"Product added: {product_name}")
                    elif action == 's':
                        product_id = int(input("Product ID to subtract: "))
                        admin.subtract_product(product_id)
                    elif action == 'q':
                        break
            else:
                print("Invalid admin credentials.")
        elif user_type == 'b':
            buyer_username = input("Buyer Username: ")
            buyer_password = input("Buyer Password: ")
            if buyer_username == buyer.username and buyer_password == buyer.password:
                while True:
                    action = input("Enter product ID to add to cart, or view cart (c/v), or proceed to checkout (p), or quit (q): ").lower()
                    if action == 'c':
                        buyer.view_cart()
                    elif action == 'p':
                        buyer.generate_bill()
                        break
                    elif action == 'q':
                        break
                    else:
                        product_id = int(action)
                        buyer.add_to_cart(product_id)
            else:
                print("Invalid buyer credentials.")
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


if __name__ == "__main__":
    main()


# In[4]:


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, discount, price):
        self.products[product_id] = {"name": product_name, "discount": discount, "price": price}

    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id):
        if product_id in self.available_products:
            self.cart.append(self.available_products[product_id])
            print(f"Product added to cart: {self.available_products[product_id]['name']}")
        else:
            print("Product not found.")

    def view_products(self):
        print("Available Products:")
        for product_id, product_info in self.available_products.items():
            print(f"Product ID: {product_id}, Product Name: {product_info['name']}")

    def view_cart(self):
        print("Products in your cart:")
        for product in self.cart:
            print(f"Product Name: {product['name']}")

    def generate_bill(self):
        total_price = 0
        print("Your Bill:")
        for product in self.cart:
            print(f"Product Name: {product['name']}, Discount: {product['discount']}%, Price: ${product['price']}")
            total_price += product['price'] * (100 - product['discount']) / 100
        print(f"Total Price: ${total_price}")


def main():
    admin = Admin("admin", "adminpass")
    admin.add_product(1, "Product1", 10, 50)
    admin.add_product(2, "Product2", 5, 30)

    buyer = Buyer("buyer", "buypass", admin.products)

    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_username = input("Admin Username: ")
            admin_password = input("Admin Password: ")
            if admin_username == admin.username and admin_password == admin.password:
                while True:
                    action = input("Add or subtract a product (a/s), or quit (q): ").lower()
                    if action == 'a':
                        num_products = int(input("How many products do you want to add: "))
                        for _ in range(num_products):
                            product_id = int(input("Product ID: "))
                            product_name = input("Product Name: ")
                            discount = int(input("Discount on the product (%): "))
                            price = float(input("Price of the product: $"))
                            admin.add_product(product_id, product_name, discount, price)
                            print(f"Product added: {product_name}")
                    elif action == 's':
                        product_id = int(input("Product ID to subtract: "))
                        admin.subtract_product(product_id)
                    elif action == 'q':
                        break
            else:
                print("Invalid admin credentials.")
        elif user_type == 'b':
            buyer_username = input("Buyer Username: ")
            buyer_password = input("Buyer Password: ")
            if buyer_username == buyer.username and buyer_password == buyer.password:
                buyer.view_products()
                while True:
                    action = input("Enter product ID to add to cart, view cart (c/v), proceed to checkout (p), or quit (q): ").lower()
                    if action == 'c':
                        buyer.view_cart()
                    elif action == 'p':
                        buyer.generate_bill()
                        break
                    elif action == 'q':
                        break
                    else:
                        product_id = int(action)
                        buyer.add_to_cart(product_id)
            else:
                print("Invalid buyer credentials.")
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


if __name__ == "__main__":
    main()


# In[2]:


import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, discount, price):
        self.products[product_id] = {"name": product_name, "discount": discount, "price": price}

    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id):
        if product_id in self.available_products:
            self.cart.append(self.available_products[product_id])
            print(f"Product added to cart: {self.available_products[product_id]['name']}")
        else:
            print("Product not found.")

    def view_products(self):
        print("Available Products:")
        for product_id, product_info in self.available_products.items():
            print(f"Product ID: {product_id}, Product Name: {product_info['name']}")

    def view_cart(self):
        print("Products in your cart:")
        for product in self.cart:
            print(f"Product Name: {product['name']}")

    def generate_bill(self):
        total_price = 0
        print("Your Bill:")
        for product in self.cart:
            print(f"Product Name: {product['name']}, Discount: {product['discount']}%, Price: ${product['price']}")
            total_price += product['price'] * (100 - product['discount']) / 100
        print(f"Total Price: ${total_price}")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    if username == admin.username and password == admin.password:
        admin_window()
    else:
        messagebox.showerror("Login Failed", "Invalid admin credentials")

def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username == buyer.username and password == buyer.password:
        buyer_window()
    else:
        messagebox.showerror("Login Failed", "Invalid buyer credentials")

def admin_window():
    admin_view.destroy()
    print("Admin logged in successfully.")
    # Rest of the admin functionality (unchanged)

def buyer_window():
    buyer_view.destroy()
    print("Buyer logged in successfully.")
    # Rest of the buyer functionality (unchanged)

# Create users and products
admin = Admin("admin", "adminpass")
admin.add_product(1, "Product1", 10, 50)
admin.add_product(2, "Product2", 5, 30)

buyer = Buyer("buyer", "buypass", admin.products)

# Create Tkinter login window for admin and user
admin_view = tk.Tk()
admin_view.title("Admin Login")

admin_username_label = tk.Label(admin_view, text="Username:")
admin_username_label.pack()
admin_username_entry = tk.Entry(admin_view)
admin_username_entry.pack()

admin_password_label = tk.Label(admin_view, text="Password:")
admin_password_label.pack()
admin_password_entry = tk.Entry(admin_view, show="*")
admin_password_entry.pack()

admin_login_button = tk.Button(admin_view, text="Login", command=admin_login)
admin_login_button.pack()

user_view = tk.Tk()
user_view.title("User Login")

user_username_label = tk.Label(user_view, text="Username:")
user_username_label.pack()
user_username_entry = tk.Entry(user_view)
user_username_entry.pack()

user_password_label = tk.Label(user_view, text="Password:")
user_password_label.pack()
user_password_entry = tk.Entry(user_view, show="*")
user_password_entry.pack()

user_login_button = tk.Button(user_view, text="Login", command=user_login)
user_login_button.pack()

admin_view.mainloop()


# In[ ]:


import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, discount, price):
        self.products[product_id] = {"name": product_name, "discount": discount, "price": price}

    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id):
        if product_id in self.available_products:
            self.cart.append(self.available_products[product_id])
            print(f"Product added to cart: {self.available_products[product_id]['name']}")
        else:
            print("Product not found.")

    def view_products(self):
        print("Available Products:")
        for product_id, product_info in self.available_products.items():
            print(f"Product ID: {product_id}, Product Name: {product_info['name']}")

    def view_cart(self):
        print("Products in your cart:")
        for product in self.cart:
            print(f"Product Name: {product['name']}")

    def generate_bill(self):
        total_price = 0
        print("Your Bill:")
        for product in self.cart:
            print(f"Product Name: {product['name']}, Discount: {product['discount']}%, Price: ${product['price']}")
            total_price += product['price'] * (100 - product['discount']) / 100
        print(f"Total Price: ${total_price}")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    if username == admin.username and password == admin.password:
        admin_view.destroy()
        admin_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid admin credentials")

def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username == buyer.username and password == buyer.password:
        user_view.destroy()
        buyer_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid buyer credentials")

def admin_cli():
    print("Admin logged in successfully.")
    while True:
        action = input("Add or subtract a product (a/s), or quit (q): ").lower()
        if action == 'a':
            num_products = int(input("How many products do you want to add: "))
            for _ in range(num_products):
                product_id = int(input("Product ID: "))
                product_name = input("Product Name: ")
                discount = int(input("Discount on the product (%): "))
                price = float(input("Price of the product: $"))
                admin.add_product(product_id, product_name, discount, price)
                print(f"Product added: {product_name}")
        elif action == 's':
            product_id = int(input("Product ID to subtract: "))
            admin.subtract_product(product_id)
        elif action == 'q':
            break

def buyer_cli():
    print("Buyer logged in successfully.")
    buyer.view_products()
    while True:
        action = input("Enter product ID to add to cart, view cart (c/v), proceed to checkout (p), or quit (q): ").lower()
        if action == 'c':
            buyer.view_cart()
        elif action == 'p':
            buyer.generate_bill()
            break
        elif action == 'q':
            break
        else:
            product_id = int(action)
            buyer.add_to_cart(product_id)

if __name__ == "__main__":
    admin = Admin("admin", "adminpass")
    admin.add_product(1, "Product1", 10, 50)
    admin.add_product(2, "Product2", 5, 30)

    buyer = Buyer("buyer", "buypass", admin.products)

    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_cli()
        elif user_type == 'b':
            buyer_cli()
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


# In[ ]:


import tkinter as tk
import os
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, discount, price):
        self.products[product_id] = {"name": product_name, "discount": discount, "price": price}

    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id):
        if product_id in self.available_products:
            self.cart.append(self.available_products[product_id])
            print(f"Product added to cart: {self.available_products[product_id]['name']}")
        else:
            print("Product not found.")

    def view_products(self):
        print("Available Products:")
        for product_id, product_info in self.available_products.items():
            print(f"Product ID: {product_id}, Product Name: {product_info['name']}")

    def view_cart(self):
        print("Products in your cart:")
        os.system('cls')
        for product in self.cart:
            print(f"Product Name: {product['name']}")

    def generate_bill(self):
        os.system('cls')
        total_price = 0
        print("Your Bill:")
        for product in self.cart:
            print(f"Product Name: {product['name']}, Discount: {product['discount']}%, Price: Rs{product['price']}")
            total_price += product['price'] * (100 - product['discount']) / 100
        print(f"Total Price: Rs{total_price}")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    if username == admin.username and password == admin.password:
        admin_login_window.destroy()
        admin_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid admin credentials")

def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username == buyer.username and password == buyer.password:
        user_login_window.destroy()
        buyer_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid buyer credentials")

def admin_cli():
    print("Admin logged in successfully.")
    while True:
        action = input("Add or subtract a product (a/s), or quit (q): ").lower()
        if action == 'a':
            num_products = int(input("How many products do you want to add: "))
            for _ in range(num_products):
                product_id = int(input("Product ID: "))
                product_name = input("Product Name: ")
                discount = int(input("Discount on the product (%): "))
                price = float(input("Price of the product: Rs"))
                admin.add_product(product_id, product_name, discount, price)
                print(f"Product added: {product_name}")
        elif action == 's':
            product_id = int(input("Product ID to subtract: "))
            admin.subtract_product(product_id)
        elif action == 'q':
            break

def buyer_cli():
    print("Buyer logged in successfully.")
    buyer.view_products()
    while True:
        action = input("Enter product ID to add to cart, view cart (c/v), proceed to checkout (p), or quit (q): ").lower()
        if action == 'c':
            buyer.view_cart()
        elif action == 'p':
            buyer.generate_bill()
            break
        elif action == 'q':
            break
        else:
            product_id = int(action)
            buyer.add_to_cart(product_id)

if __name__ == "__main__":
    admin = Admin("admin", "adminpass")
   

    buyer = Buyer("buyer", "buypass", admin.products)

    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_login_window = tk.Tk()
            admin_login_window.title("Admin Login")

            admin_username_label = tk.Label(admin_login_window, text="Username:")
            admin_username_label.pack()
            admin_username_entry = tk.Entry(admin_login_window)
            admin_username_entry.pack()

            admin_password_label = tk.Label(admin_login_window, text="Password:")
            admin_password_label.pack()
            admin_password_entry = tk.Entry(admin_login_window, show="*")
            admin_password_entry.pack()

            admin_login_button = tk.Button(admin_login_window, text="Login", command=admin_login)
            admin_login_button.pack()

            admin_login_window.mainloop()
        elif user_type == 'b':
            user_login_window = tk.Tk()
            user_login_window.title("User Login")

            user_username_label = tk.Label(user_login_window, text="Username:")
            user_username_label.pack()
            user_username_entry = tk.Entry(user_login_window)
            user_username_entry.pack()

            user_password_label = tk.Label(user_login_window, text="Password:")
            user_password_label.pack()
            user_password_entry = tk.Entry(user_login_window, show="*")
            user_password_entry.pack()

            user_login_button = tk.Button(user_login_window, text="Login", command=user_login)
            user_login_button.pack()

            user_login_window.mainloop()
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


# In[ ]:


import tkinter as tk
import os
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, discount, price):
        self.products[product_id] = {"name": product_name, "discount": discount, "price": price}

    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id):
        if product_id in self.available_products:
            self.cart.append(self.available_products[product_id])
            print(f"Product added to cart: {self.available_products[product_id]['name']}")
        else:
            print("Product not found.")

    def view_products(self):
        print("Available Products:")
        for product_id, product_info in self.available_products.items():
            print(f"Product ID: {product_id}, Product Name: {product_info['name']}")

    def view_cart(self):
        print("Products in your cart:")
        os.system('cls')
        for product in self.cart:
            print(f"Product Name: {product['name']}")

    def generate_bill(self):
        os.system('cls')
        total_price = 0
        print("Your Bill:")
        for product in self.cart:
            print(f"Product Name: {product['name']}, Discount: {product['discount']}%, Price: Rs{product['price']}")
            total_price += product['price'] * (100 - product['discount']) / 100
        print(f"Total Price: Rs{total_price}")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    if username == admin.username and password == admin.password:
        admin_login_window.destroy()
        admin_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid admin credentials")

def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username == buyer.username and password == buyer.password:
        user_login_window.destroy()
        buyer_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid buyer credentials")

def admin_cli():
    print("Admin logged in successfully.")
    while True:
        action = input("Add or subtract a product (a/s), or quit (q): ").lower()
        if action == 'a':
            num_products = int(input("How many products do you want to add: "))
            for _ in range(num_products):
                product_id = int(input("Product ID: "))
                product_name = input("Product Name: ")
                discount = int(input("Discount on the product (%): "))
                price = float(input("Price of the product: Rs"))
                admin.add_product(product_id, product_name, discount, price)
                print(f"Product added: {product_name}")
        elif action == 's':
            product_id = int(input("Product ID to subtract: "))
            admin.subtract_product(product_id)
        elif action == 'q':
            break

def buyer_cli():
    print("Buyer logged in successfully.")
    buyer.view_products()
    while True:
        action = input("Enter product ID to add to cart, view cart (c/v), proceed to checkout (p), or quit (q): ").lower()
        if action == 'c':
            buyer.view_cart()
        elif action == 'p':
            buyer.generate_bill()
            break
        elif action == 'q':
            break
        else:
            product_id = int(action)
            buyer.add_to_cart(product_id)

if __name__ == "__main__":
    admin = Admin("admin", "adminpass")
   

    buyer = Buyer("buyer", "buypass", admin.products)

    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_login_window = tk.Tk()
            admin_login_window.title("Admin Login")

            admin_username_label = tk.Label(admin_login_window, text="Username:")
            admin_username_label.pack()
            admin_username_entry = tk.Entry(admin_login_window)
            admin_username_entry.pack()

            admin_password_label = tk.Label(admin_login_window, text="Password:")
            admin_password_label.pack()
            admin_password_entry = tk.Entry(admin_login_window, show="*")
            admin_password_entry.pack()

            admin_login_button = tk.Button(admin_login_window, text="Login", command=admin_login)
            admin_login_button.pack()

            admin_login_window.mainloop()
        elif user_type == 'b':
            user_login_window = tk.Tk()
            user_login_window.title("User Login")

            user_username_label = tk.Label(user_login_window, text="Username:")
            user_username_label.pack()
            user_username_entry = tk.Entry(user_login_window)
            user_username_entry.pack()

            user_password_label = tk.Label(user_login_window, text="Password:")
            user_password_label.pack()
            user_password_entry = tk.Entry(user_login_window, show="*")
            user_password_entry.pack()

            user_login_button = tk.Button(user_login_window, text="Login", command=user_login)
            user_login_button.pack()

            user_login_window.mainloop()
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


# In[ ]:


import tkinter as tk
import os
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, discount, price):
        if product_id in self.products:
            print("A product with the same ID already exists. Please enter a unique product ID.")
            return
        self.products[product_id] = {"name": product_name, "discount": discount, "price": price}

    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id):
        if product_id in self.available_products:
            self.cart.append(self.available_products[product_id])
            print(f"Product added to cart: {self.available_products[product_id]['name']}")
        else:
            print("Product not found.")

    def view_products(self):
        print("Available Products:")
        for product_id, product_info in self.available_products.items():
            print(f"Product ID: {product_id}, Product Name: {product_info['name']}")

    def view_cart(self):
        os.system('cls')
        print("Products in your cart:")
        for product in self.cart:
            print(f"Product Name: {product['name']}")

    def generate_bill(self):
        os.system('cls')
        total_price = 0
        print("Your Bill:")
        for product in self.cart:
            print(f"Product Name: {product['name']}, Discount: {product['discount']}%, Price: Rs{product['price']}")
            total_price += product['price'] * (100 - product['discount']) / 100
        print(f"Total Price: Rs{total_price}")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    if username == admin.username and password == admin.password:
        admin_login_window.destroy()
        admin_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid admin credentials")

def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username == buyer.username and password == buyer.password:
        user_login_window.destroy()
        buyer_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid buyer credentials")

def admin_cli():
    print("Admin logged in successfully.")
    while True:
        action = input("Add or subtract a product (a/s), or quit (q): ").lower()
        if action == 'a':
            num_products = int(input("How many products do you want to add: "))
            for _ in range(num_products):
                product_id = int(input("Product ID: "))
                while product_id in admin.products:
                    print("A product with the same ID already exists. Please enter a unique product ID.")
                    product_id = int(input("Product ID: "))
                product_name = input("Product Name: ")
                discount = int(input("Discount on the product (%): "))
                price = float(input("Price of the product: Rs"))
                admin.add_product(product_id, product_name, discount, price)
                print(f"Product added: {product_name}")
        elif action == 's':
            product_id = int(input("Product ID to subtract: "))
            admin.subtract_product(product_id)
        elif action == 'q':
            break

def buyer_cli():
    print("Buyer logged in successfully.")
    buyer.view_products()
    while True:
        action = input("Enter product ID to add to cart, view cart (c/v), proceed to checkout (p), or quit (q): ").lower()
        if action == 'c':
            buyer.view_cart()
        elif action == 'p':
            buyer.generate_bill()
            break
        elif action == 'q':
            break
        else:
            product_id = int(action)
            buyer.add_to_cart(product_id)

if __name__ == "__main__":
    admin = Admin("admin", "adminpass")
   

    buyer = Buyer("buyer", "buypass", admin.products)

    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_login_window = tk.Tk()
            admin_login_window.title("Admin Login")

            admin_username_label = tk.Label(admin_login_window, text="Admin Username:")
            admin_username_label.pack()
            admin_username_entry = tk.Entry(admin_login_window)
            admin_username_entry.pack()

            admin_password_label = tk.Label(admin_login_window, text="Admin Password:")
            admin_password_label.pack()
            admin_password_entry = tk.Entry(admin_login_window, show="*")
            admin_password_entry.pack()

            admin_login_button = tk.Button(admin_login_window, text="Login", command=admin_login)
            admin_login_button.pack()

            admin_login_window.mainloop()
        elif user_type == 'b':
            user_login_window = tk.Tk()
            user_login_window.title("Buyer Login")

            user_username_label = tk.Label(user_login_window, text="Buyer Username:")
            user_username_label.pack()
            user_username_entry = tk.Entry(user_login_window)
            user_username_entry.pack()

            user_password_label = tk.Label(user_login_window, text="Buyer Password:")
            user_password_label.pack()
            user_password_entry = tk.Entry(user_login_window, show="*")
            user_password_entry.pack()

            user_login_button = tk.Button(user_login_window, text="Login", command=user_login)
            user_login_button.pack()

            user_login_window.mainloop()
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


# In[ ]:


import tkinter as tk
import os
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, discount, price, quantity):
        if product_id in self.products:
            print("A product with the same ID already exists. Please enter a unique product ID.")
            return
        self.products[product_id] = {"name": product_name, "discount": discount, "price": price, "quantity": quantity}

    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id, quantity):
        if product_id in self.available_products:
            product = self.available_products[product_id]
            if quantity <= product['quantity']:
                self.cart.append({"product": product, "quantity": quantity})
                print(f"{quantity} {product['name']} added to cart")
            else:
                print(f"Insufficient quantity of {product['name']} in stock.")
        else:
            print("Product not found.")

    def view_products(self):
        print("Available Products:")
        for product_id, product_info in self.available_products.items():
            print(f"Product ID: {product_id}, Product Name: {product_info['name']}, Quantity: {product_info['quantity']}, Price: Rs{product_info['price']}")

    def view_cart(self):
        os.system('cls')
        print("Products in your cart:")
        for item in self.cart:
            product = item['product']
            quantity = item['quantity']
            print(f"{quantity} {product['name']} in cart")

    def generate_bill(self):
        os.system('cls')
        total_price = 0
        print("Your Bill:")
        for item in self.cart:
            product = item['product']
            quantity = item['quantity']
            print(f"{quantity} {product['name']}, Discount: {product['discount']}%, Price: Rs{product['price']} each")
            total_price += (product['price'] * (100 - product['discount']) / 100) * quantity
            # Update the product quantity
            product['quantity'] -= quantity
        print(f"Total Price: Rs{total_price}")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    if username == admin.username and password == admin.password:
        admin_login_window.destroy()
        admin_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid admin credentials")

def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username == buyer.username and password == buyer.password:
        user_login_window.destroy()
        buyer_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid buyer credentials")

def admin_cli():
    print("Admin logged in successfully.")
    while True:
        action = input("Add or subtract a product (a/s), or quit (q): ").lower()
        if action == 'a':
            num_products = int(input("How many products do you want to add: "))
            for _ in range(num_products):
                product_id = int(input("Product ID: "))
                while product_id in admin.products:
                    print("A product with the same ID already exists. Please enter a unique product ID.")
                    product_id = int(input("Product ID: "))
                product_name = input("Product Name: ")
                discount = int(input("Discount on the product (%): "))
                price = float(input("Price of the product: Rs"))
                quantity = int(input("Quantity in stock: "))
                admin.add_product(product_id, product_name, discount, price, quantity)
                print(f"Product added: {product_name}")
        elif action == 's':
            product_id = int(input("Product ID to subtract: "))
            admin.subtract_product(product_id)
        elif action == 'q':
            break

def buyer_cli():
    print("Buyer logged in successfully.")
    buyer.view_products()
    while True:
        action = input("Enter product ID to add to cart, view cart (c/v), proceed to checkout (p), or quit (q): ").lower()
        if action == 'c':
            buyer.view_cart()
        elif action == 'p':
            buyer.generate_bill()
            break
        elif action == 'q':
            break
        else:
            product_id = int(action)
            quantity = int(input(f"Enter quantity of {buyer.available_products[product_id]['name']} you want to add to the cart: "))
            buyer.add_to_cart(product_id, quantity)

if __name__ == "__main__":
    admin = Admin("admin", "adminpass")
   

    buyer = Buyer("buyer", "buypass", admin.products)

    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_login_window = tk.Tk()
            admin_login_window.title("Admin Login")

            admin_username_label = tk.Label(admin_login_window, text="Username:")
            admin_username_label.pack()
            admin_username_entry = tk.Entry(admin_login_window)
            admin_username_entry.pack()

            admin_password_label = tk.Label(admin_login_window, text="Password:")
            admin_password_label.pack()
            admin_password_entry = tk.Entry(admin_login_window, show="*")
            admin_password_entry.pack()

            admin_login_button = tk.Button(admin_login_window, text="Login", command=admin_login)
            admin_login_button.pack()

            admin_login_window.mainloop()
        elif user_type == 'b':
            user_login_window = tk.Tk()
            user_login_window.title("User Login")

            user_username_label = tk.Label(user_login_window, text="Username:")
            user_username_label.pack()
            user_username_entry = tk.Entry(user_login_window)
            user_username_entry.pack()

            user_password_label = tk.Label(user_login_window, text="Password:")
            user_password_label.pack()
            user_password_entry = tk.Entry(user_login_window, show="*")
            user_password_entry.pack()

            user_login_button = tk.Button(user_login_window, text="Login", command=user_login)
            user_login_button.pack()

            user_login_window.mainloop()
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


# In[1]:


import tkinter as tk
import os
from tkinter import messagebox

class User:
    def __init(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, price, discount, min_quantity_for_discount):
        if product_id in self.products:
            print("A product with the same ID already exists. Please enter a unique product ID.")
            return
        self.products[product_id] = {"name": product_name, "price": price, "discount": discount, "min_quantity_for_discount": min_quantity_for_discount, "quantity": 0}

    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id, quantity):
        if product_id in self.available_products:
            product = self.available_products[product_id]
            self.cart.append({"product": product, "quantity": quantity})
            print(f"{quantity} {product['name']} added to cart")
        else:
            print("Product not found.")

    def view_products(self):
        print("Available Products:")
        for product_id, product_info in self.available_products.items():
            discount_info = f", Discount: {product_info['discount']}%, Min Quantity for Discount: {product_info['min_quantity_for_discount']}" if product_info['min_quantity_for_discount'] > 0 else ""
            print(f"Product ID: {product_id}, Product Name: {product_info['name']}, Price: Rs{product_info['price']}{discount_info}")

    def view_cart(self):
        os.system('cls')
        print("Products in your cart:")
        for item in self.cart:
            product = item['product']
            quantity = item['quantity']
            print(f"{quantity} {product['name']} in cart")

    def generate_bill(self):
        os.system('cls')
        total_price = 0
        print("Your Bill:")
        for item in self.cart:
            product = item['product']
            quantity = item['quantity']
            discount = product['discount'] if quantity >= product['min_quantity_for_discount'] else 0
            print(f"{quantity} {product['name']}, Discount: {discount}%, Price: Rs{product['price']} each")
            total_price += (product['price'] * (100 - discount) / 100) * quantity
            # Update the product quantity
            product['quantity'] -= quantity
        print(f"Total Price: Rs{total_price}")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    if username == admin.username and password == admin.password:
        admin_login_window.destroy()
        admin_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid admin credentials")

def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username == buyer.username and password == buyer.password:
        user_login_window.destroy()
        buyer_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid buyer credentials")

def admin_cli():
    print("Admin logged in successfully.")
    while True:
        action = input("Add or subtract a product (a/s), or quit (q): ").lower()
        if action == 'a':
            num_products = int(input("How many products do you want to add: "))
            for _ in range(num_products):
                product_id = int(input("Product ID: "))
                while product_id in admin.products:
                    print("A product with the same ID already exists. Please enter a unique product ID.")
                    product_id = int(input("Product ID: "))
                product_name = input("Product Name: ")
                price = float(input("Price of the product: Rs"))
                discount = int(input("Discount on the product (%): "))
                min_quantity_for_discount = int(input("Minimum Quantity for Discount: "))
                admin.add_product(product_id, product_name, price, discount, min_quantity_for_discount)
                print(f"Product added: {product_name}")
        elif action == 's':
            product_id = int(input("Product ID to subtract: "))
            admin.subtract_product(product_id)
        elif action == 'q':
            break

def buyer_cli():
    print("Buyer logged in successfully.")
    buyer.view_products()
    while True:
        action = input("Enter product ID to add to cart, view cart (c/v), proceed to checkout (p), or quit (q): ").lower()
        if action == 'c':
            buyer.view_cart()
        elif action == 'p':
            buyer.generate_bill()
            break
        elif action == 'q':
            break
        else:
            product_id = int(action)
            quantity = int(input(f"Enter quantity of {buyer.available_products[product_id]['name']} you want to add to the cart: "))
            buyer.add_to_cart(product_id, quantity)

if __name__ == "__main__":
    admin = Admin("admin", "adminpass")
   

    buyer = Buyer("buyer", "buypass", admin.products)

    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_login_window = tk.Tk()
            admin_login_window.title("Admin Login")

            admin_username_label = tk.Label(admin_login_window, text="Username:")
            admin_username_label.pack()
            admin_username_entry = tk.Entry(admin_login_window)
            admin_username_entry.pack()

            admin_password_label = tk.Label(admin_login_window, text="Password:")
            admin_password_label.pack()
            admin_password_entry = tk.Entry(admin_login_window, show="*")
            admin_password_entry.pack()

            admin_login_button = tk.Button(admin_login_window, text="Login", command=admin_login)
            admin_login_button.pack()

            admin_login_window.mainloop()
        elif user_type == 'b':
            user_login_window = tk.Tk()
            user_login_window.title("User Login")

            user_username_label = tk.Label(user_login_window, text="Username:")
            user_username_label.pack()
            user_username_entry = tk.Entry(user_login_window)
            user_username_entry.pack()

            user_password_label = tk.Label(user_login_window, text="Password:")
            user_password_label.pack()
            user_password_entry = tk.Entry(user_login_window, show="*")
            user_password_entry.pack()

            user_login_button = tk.Button(user_login_window, text="Login", command=user_login)
            user_login_button.pack()

            user_login_window.mainloop()
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


# In[ ]:


import tkinter as tk
import os
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = {}

    def add_product(self, product_id, product_name, price, discount, min_quantity_for_discount, quantity):
        if product_id in self.products:
            print("A product with the same ID already exists. Please enter a unique product ID.")
            return
        self.products[product_id] = {
            "name": product_name,
            "price": price,
            "discount": discount,
            "min_quantity_for_discount": min_quantity_for_discount,
            "quantity": quantity,
        }
        
    def subtract_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found.")

class Buyer(User):
    def __init__(self, username, password, products):
        super().__init__(username, password)
        self.cart = []
        self.available_products = products

    def add_to_cart(self, product_id, quantity):
        if product_id in self.available_products:
            product = self.available_products[product_id]
            self.cart.append({"product": product, "quantity": quantity})
            print(f"{quantity} {product['name']} added to cart")
        else:
            print("Product not found.")

    def view_products(self):
        print("Available Products:")
        for product_id, product_info in self.available_products.items():
            discount_info = f", Discount: {product_info['discount']}%, Min Quantity for Discount: {product_info['min_quantity_for_discount']}" if product_info['min_quantity_for_discount'] > 0 else ""
            print(f"Product ID: {product_id}, Product Name: {product_info['name']}, Price: Rs{product_info['price']}{discount_info}, Quantity in Stock: {product_info['quantity']}")

    def view_cart(self):
        os.system('cls')
        print("Products in your cart:")
        for item in self.cart:
            product = item['product']
            quantity = item['quantity']
            print(f"{quantity} {product['name']} in cart")

    def generate_bill(self):
        os.system('cls')
        total_price = 0
        print("Your Bill:")
        for item in self.cart:
            product = item['product']
            quantity = item['quantity']
            discount = product['discount'] if quantity >= product['min_quantity_for_discount'] else 0
            print(f"{quantity} {product['name']}, Discount: {discount}%, Price: Rs{product['price']} each")
            total_price += (product['price'] * (100 - discount) / 100) * quantity
            # Update the product quantity
            product['quantity'] -= quantity
            tax = total_price* 0.10
        print(f"10% tax added : Rs{tax}")
        print(f"Total Price: Rs{total_price + tax}")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    if username == admin.username and password == admin.password:
        admin_login_window.destroy()
        admin_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid admin credentials")

def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username == buyer.username and password == buyer.password:
        user_login_window.destroy()
        buyer_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid buyer credentials")

def admin_cli():
    print("Admin logged in successfully.")
    while True:
        action = input("Add or subtract a product (a/s), or quit (q): ").lower()
        if action == 'a':
            num_products = int(input("How many products do you want to add: "))
            for _ in range(num_products):
                product_id = int(input("Product ID: "))
                while product_id in admin.products:
                    print("A product with the same ID already exists. Please enter a unique product ID.")
                    product_id = int(input("Product ID: "))
                product_name = input("Product Name: ")
                price = float(input("Price of the product: Rs"))
                discount = int(input("Discount on the product (%): "))
                min_quantity_for_discount = int(input("Minimum Quantity for Discount: "))
                quantity = int(input("Quantity in stock: "))  # New input for quantity
                admin.add_product(product_id, product_name, price, discount, min_quantity_for_discount, quantity)
                print(f"Product added: {product_name}")
        elif action == 's':
            product_id = int(input("Product ID to subtract: "))
            admin.subtract_product(product_id)
        elif action == 'q':
            break


def buyer_cli():
    print("Buyer logged in successfully.")
    buyer.view_products()
    while True:
        action = input("Enter product ID to add to cart, view cart (c/v), proceed to checkout (p), or quit (q): ").lower()
        if action == 'c':
            buyer.view_cart()
        elif action == 'p':
            buyer.generate_bill()
            break
        elif action == 'q':
            break
        else:
            product_id = int(action)
            if product_id in buyer.available_products:
                quantity = int(input(f"Enter quantity of {buyer.available_products[product_id]['name']} you want to add to the cart: "))
                buyer.add_to_cart(product_id, quantity)
            else:
                print("Product not found.")


if __name__ == "__main__":
    admin = Admin("admin", "adminpass")
    buyer = Buyer("buyer", "buypass", admin.products)
    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_login_window = tk.Tk()
            admin_login_window.title("Admin Login")

            admin_username_label = tk.Label(admin_login_window, text="Username:")
            admin_username_label.pack()
            admin_username_entry = tk.Entry(admin_login_window)
            admin_username_entry.pack()

            admin_password_label = tk.Label(admin_login_window, text="Password:")
            admin_password_label.pack()
            admin_password_entry = tk.Entry(admin_login_window, show="*")
            admin_password_entry.pack()

            admin_login_button = tk.Button(admin_login_window, text="Login", command=admin_login)
            admin_login_button.pack()

            admin_login_window.mainloop()
        elif user_type == 'b':
            user_login_window = tk.Tk()
            user_login_window.title("User Login")

            user_username_label = tk.Label(user_login_window, text="Username:")
            user_username_label.pack()
            user_username_entry = tk.Entry(user_login_window)
            user_username_entry.pack()

            user_password_label = tk.Label(user_login_window, text="Password:")
            user_password_label.pack()
            user_password_entry = tk.Entry(user_login_window, show="*")
            user_password_entry.pack()

            user_login_button = tk.Button(user_login_window, text="Login", command=user_login)
            user_login_button.pack()

            user_login_window.mainloop()
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


# In[ ]:


import tkinter as tk
import os
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.categories = {}  # Dictionary to store categories and their products

    def add_category(self, category_name):
        if category_name in self.categories:
            print("Category already exists. Please enter a unique category name.")
        else:
            self.categories[category_name] = []

    def add_product(self, category_name, product_id, product_name, price, discount, min_quantity_for_discount, quantity):
        if category_name not in self.categories:
            print("Category not found. Please create the category first.")
        else:
            category = self.categories[category_name]
            if product_id in category:
                print("A product with the same ID already exists in this category. Please enter a unique product ID.")
            else:
                category.append({
                    "product_id": product_id,
                    "name": product_name,
                    "price": price,
                    "discount": discount,
                    "min_quantity_for_discount": min_quantity_for_discount,
                    "quantity": quantity,
                })

    def subtract_product(self, category_name, product_id):
        if category_name not in self.categories:
            print("Category not found.")
        else:
            category = self.categories[category_name]
            for product in category:
                if product["product_id"] == product_id:
                    category.remove(product)
                    return
            print("Product not found in the category.")

class Buyer(User):
    def __init__(self, username, password, categories):
        super().__init__(username, password)
        self.cart = []
        self.available_categories = categories

    def view_categories(self):
        print("Available Categories:")
        for category_name in self.available_categories:
            print(category_name)

    def view_products(self, category_name):
        if category_name not in self.available_categories:
            print("Category not found.")
        else:
            category = self.available_categories[category_name]
            print(f"Products in Category: {category_name}")
            for product in category:
                discount_info = f", Discount: {product['discount']}%, Min Quantity for Discount: {product['min_quantity_for_discount']}" if product['min_quantity_for_discount'] > 0 else ""
                print(f"Product ID: {product['product_id']}, Product Name: {product['name']}, Price: Rs{product['price']}{discount_info}, Quantity in Stock: {product['quantity']}")

    def view_cart(self):
        os.system('cls')
        print("Products in your cart:")
        for item in self.cart:
            product = item['product']
            quantity = item['quantity']
            print(f"{quantity} {product['name']} in cart")

    def generate_bill(self):
        os.system('cls')
        total_price = 0
        print("Your Bill:")
        for item in self.cart:
            product = item['product']
            quantity = item['quantity']
            discount = product['discount'] if quantity >= product['min_quantity_for_discount'] else 0
            print(f"{quantity} {product['name']}, Discount: {discount}%, Price: Rs{product['price']} each")
            total_price += (product['price'] * (100 - discount) / 100) * quantity
            # Update the product quantity
            product['quantity'] -= quantity
            tax = total_price* 0.10
        print(f"10% tax added : Rs{tax}")
        print(f"Total Price: Rs{total_price + tax}")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    if username == admin.username and password == admin.password:
        admin_login_window.destroy()
        admin_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid admin credentials")

def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username == buyer.username and password == buyer.password:
        user_login_window.destroy()
        buyer_cli()
    else:
        messagebox.showerror("Login Failed", "Invalid buyer credentials")

def admin_cli():
    print("Admin logged in successfully.")
    while True:
        action = input("Add, subtract a category or product (ac/ap/sc/sp), or quit (q): ").lower()
        if action == 'ac':
            category_name = input("Category Name: ")
            admin.add_category(category_name)
        elif action == 'ap':
            category_name = input("Category Name: ")
            num_products = int(input("How many products do you want to add to this category: "))
            for _ in range(num_products):
                product_id = int(input("Product ID: "))
                while any(product["product_id"] == product_id for product in admin.categories[category_name]):
                    print("A product with the same ID already exists in this category. Please enter a unique product ID.")
                    product_id = int(input("Product ID: "))
                product_name = input("Product Name: ")
                price = float(input("Price of the product: Rs"))
                discount = int(input("Discount on the product (%): "))
                min_quantity_for_discount = int(input("Minimum Quantity for Discount: "))
                quantity = int(input("Quantity in stock: "))  # New input for quantity
                admin.add_product(category_name, product_id, product_name, price, discount, min_quantity_for_discount, quantity)
                print(f"Product added to category {category_name}: {product_name}")
        elif action == 'sc':
            category_name = input("Category Name: ")
            if category_name in admin.categories:
                del admin.categories[category_name]
                print(f"Category {category_name} removed.")
            else:
                print("Category not found.")
        elif action == 'sp':
            category_name = input("Category Name: ")
            if category_name in admin.categories:
                product_id = int(input("Product ID to subtract from the category: "))
                admin.subtract_product(category_name, product_id)
            else:
                print("Category not found.")
        elif action == 'q':
            break

def buyer_cli():
    print("Buyer logged in successfully.")
    buyer.view_categories()
    while True:
        category_name = input("Enter category name to view products, view cart (c/v), proceed to checkout (p), or quit (q): ")
        if category_name == 'c':
            buyer.view_cart()
        elif category_name == 'p':
            buyer.generate_bill()
            break
        elif category_name == 'q':
            break
        elif category_name in buyer.available_categories:
            buyer.view_products(category_name)
            product_id = int(input("Enter product ID to add to cart: "))
            quantity = int(input(f"Enter quantity of the product you want to add to the cart: "))
            buyer.add_to_cart(category_name, product_id, quantity)
        else:
            print("Category not found.")

if __name__ == "__main__":
    # Create categories and products for admin
    admin = Admin("admin", "adminpass")
    admin.add_category("Electronics")
    admin.add_product("Electronics", 1, "Laptop", 1000, 5, 2, 10)
    admin.add_product("Electronics", 2, "Smartphone", 500, 10, 3, 15)
    admin.add_category("Clothing")
    admin.add_product("Clothing", 3, "T-Shirt", 20, 2, 4, 50)
    admin.add_product("Clothing", 4, "Jeans", 50, 0, 0, 25)

    # Create categories for the buyer
    buyer_categories = admin.categories

    buyer = Buyer("buyer", "buypass", buyer_categories)

    while True:
        user_type = input("Login as admin or buyer (a/b): ").lower()
        if user_type == 'a':
            admin_login_window = tk.Tk()
            admin_login_window.title("Admin Login")

            admin_username_label = tk.Label(admin_login_window, text="Username:")
            admin_username_label.pack()
            admin_username_entry = tk.Entry(admin_login_window)
            admin_username_entry.pack()

            admin_password_label = tk.Label(admin_login_window, text="Password:")
            admin_password_label.pack()
            admin_password_entry = tk.Entry(admin_login_window, show="*")
            admin_password_entry.pack()

            admin_login_button = tk.Button(admin_login_window, text="Login", command=admin_login)
            admin_login_button.pack()

            admin_login_window.mainloop()
        elif user_type == 'b':
            user_login_window = tk.Tk()
            user_login_window.title("User Login")

            user_username_label = tk.Label(user_login_window, text="Username:")
            user_username_label.pack()
            user_username_entry = tk.Entry(user_login_window)
            user_username_entry.pack()

            user_password_label = tk.Label(user_login_window, text="Password:")
            user_password_label.pack()
            user_password_entry = tk.Entry(user_login_window, show="*")
            user_password_entry.pack()

            user_login_button = tk.Button(user_login_window, text="Login", command=user_login)
            user_login_button.pack()

            user_login_window.mainloop()
        else:
            print("Invalid choice. Please enter 'a' for admin or 'b' for buyer.")


# In[ ]:




