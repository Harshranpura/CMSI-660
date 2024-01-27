import uuid
import re


class ShoppingCart:
    def __init__(self, customer_id):
        # Generate a unique cart id using uuid4
        self.cart_id = str(uuid.uuid4())
        # Validate and set the customer id
        self.set_customer_id(customer_id)
        # Initialize an empty cart as a dictionary to store items and quantities
        self.cart_items = {}

    def set_customer_id(self, customer_id):
        # Validate the customer id format
        if self.validate_customer_id(customer_id):
            self.customer_id = customer_id
        else:
            raise ValueError("Invalid customer id format")

    def validate_customer_id(self, customer_id):
    # Define a regular expression pattern for the customer id format
     pattern = r'^[A-Z]{3}\d{5}[A-Z]{2}[-][AQ]$'
    
    # Use the re.match() function to check if the customer_id matches the pattern
     if re.match(pattern, customer_id):
        return True
     else:
        return False
       

    def get_cart_id(self):
        return self.cart_id

    def get_customer_id(self):
        return self.customer_id

    def get_items(self):
        # Return a copy of the cart_items dictionary to ensure immutability
        return self.cart_items.copy()

    def add_item(self, item_name, quantity, price, catalog):
    # Check if the item is in the catalog
     if item_name not in catalog:
        raise ValueError("Item not found in the catalog")
    
    # Validate item name and quantity
     if not self.validate_item_name(item_name):
        raise ValueError("Invalid item name format")
    
     if not self.validate_quantity(quantity):
        raise ValueError("Invalid quantity")
    
    # Ensure immutability by creating a new dictionary with the updated items
     updated_cart = self.cart_items.copy()
    
    # Check if the item is already in the cart
     if item_name in updated_cart:
        updated_cart[item_name] += quantity
     else:
        updated_cart[item_name] = quantity
    
    # Update the cart_items with the new dictionary
     self.cart_items = updated_cart

    def update_item(self, item_name, new_quantity):
    # Ensure immutability by creating a new dictionary with the updated items
     updated_cart = self.cart_items.copy()

    # Check if the item_name exists in the cart
     if item_name in updated_cart:
        # Validate the new_quantity
        if not self.validate_quantity(new_quantity):
            raise ValueError("Invalid quantity")

        # Update the quantity of the existing item in the cart
        updated_cart[item_name] = new_quantity
     else:
        raise ValueError("Item not found in the cart")

    # Update the cart_items with the new dictionary
     self.cart_items = updated_cart


    def remove_item(self, item_name):
    # Ensure immutability by creating a new dictionary without the removed item
     updated_cart = self.cart_items.copy()

    # Check if the item_name exists in the cart
     if item_name in updated_cart:
        # Remove the item from the updated cart
        del updated_cart[item_name]
     else:
        raise ValueError("Item not found in the cart")

    # Update the cart_items with the new dictionary
     self.cart_items = updated_cart

    def get_total_cost(self, catalog):
     total_cost = 0

    # Iterate through items in the cart and calculate the total cost
     for item_name, quantity in self.cart_items.items():
        # Check if the item is in the catalog
        if item_name not in catalog:
            raise ValueError(f"Item '{item_name}' not found in the catalog")

        # Validate quantity to ensure it's non-negative
        if quantity < 0:
            raise ValueError("Negative quantity in the cart")

        # Calculate the cost of the item and add it to the total cost
        item_cost = catalog[item_name] * quantity
        total_cost += item_cost

     return total_cost


    def validate_item_name(self, item_name):
    # Define the maximum allowed length for item names
     max_name_length = 50  # You can adjust this value based on your requirements
    
    # Check if the item name is a string and within the character limit
     if isinstance(item_name, str) and len(item_name) <= max_name_length:
        # Implement additional checks if needed, e.g., character restrictions
        # For example, if you want to allow only alphanumeric characters and spaces:
        if item_name.isalnum() or ' ' in item_name:
            return True

     return False
    def validate_quantity(self, quantity):
        # Check if the quantity is a non-negative integer
        if isinstance(quantity, int) and quantity >= 0:
            return True

        return False
class Catalog:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def remove_item(self, item_name):
        del self.items[item_name]

    def get_catalog(self):
        return self.items.copy()
    
# Create an instance of the Catalog class
catalog = Catalog()

# Add items to the catalog
catalog.add_item("ItemA", 10.99)
catalog.add_item("ItemB", 5.99)
catalog.add_item("ItemC", 7.49)

# Create an instance of the ShoppingCart class with a valid customer id
cart = ShoppingCart("ABC12345DE-A")

# Add items to the shopping cart
cart.add_item("ItemA", 2, 10.99, catalog.get_catalog())
cart.add_item("ItemB", 3, 5.99, catalog.get_catalog())
# Update the quantity of an item in the shopping cart
cart.update_item("ItemA", 5)

# Remove an item from the shopping cart
cart.remove_item("ItemB")

# Calculate and print the total cost
total_cost = cart.get_total_cost(catalog.get_catalog())
print(f"Total cost of items in the cart: ${total_cost:.2f}")