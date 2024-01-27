import unittest

# Import the ShoppingCart and Catalog classes from the cart.py file inside the cart_package module
from cart_package.cart import ShoppingCart, Catalog

# Define a test class for ShoppingCart, inheriting from unittest.TestCase
class TestShoppingCart(unittest.TestCase):

    # Test case to check if ShoppingCart is initialized correctly
    def test_cart_initialization_valid(self):
        cart = ShoppingCart("ABC12345DE-A")
        # Assert that an instance of ShoppingCart is created
        self.assertIsInstance(cart, ShoppingCart)
    
    # Test case to check if a ValueError is raised with an invalid customer ID
    def test_invalid_customer_id_format(self):
        with self.assertRaises(ValueError):
            ShoppingCart("invalid_id")

    # Test case to check if an item can be added to the shopping cart
    def test_add_item_to_cart(self):
        catalog = Catalog()
        catalog.add_item("ItemA", 10.99)
        cart = ShoppingCart("ABC12345DE-A")
        cart.add_item("ItemA", 2, 10.99, catalog.get_catalog())
        # Assert that the item was added correctly
        self.assertEqual(cart.get_items(), {"ItemA": 2})

    # Test case to check if an item's quantity can be updated in the cart
    def test_update_item_quantity(self):
        catalog = Catalog()
        catalog.add_item("ItemA", 10.99)
        cart = ShoppingCart("ABC12345DE-A")
        cart.add_item("ItemA", 2, 10.99, catalog.get_catalog())
        cart.update_item("ItemA", 5)
        # Assert that the item quantity was updated correctly
        self.assertEqual(cart.get_items(), {"ItemA": 5})

    # Test case to check if an item can be removed from the cart
    def test_remove_item_from_cart(self):
        catalog = Catalog()
        catalog.add_item("ItemA", 10.99)
        cart = ShoppingCart("ABC12345DE-A")
        cart.add_item("ItemA", 2, 10.99, catalog.get_catalog())
        cart.remove_item("ItemA")
        # Assert that the item was removed correctly
        self.assertEqual(cart.get_items(), {})

    # Test case to check the total cost calculation in the cart
    def test_total_cost_calculation(self):
        catalog = Catalog()
        catalog.add_item("ItemA", 10.99)
        catalog.add_item("ItemB", 5.99)
        cart = ShoppingCart("ABC12345DE-A")
        cart.add_item("ItemA", 2, 10.99, catalog.get_catalog())
        cart.add_item("ItemB", 3, 5.99, catalog.get_catalog())
        total_cost = cart.get_total_cost(catalog.get_catalog())
        # Assert that the total cost is calculated correctly
        self.assertAlmostEqual(total_cost, 39.95, places=2)

# Define a test class for Catalog, inheriting from unittest.TestCase
class TestCatalog(unittest.TestCase):

    # Test case to check if Catalog is initialized correctly
    def test_catalog_initialization(self):
        catalog = Catalog()
        # Assert that an instance of Catalog is created
        self.assertIsInstance(catalog, Catalog)

    # Test case to check if an item can be added to the catalog
    def test_add_item_to_catalog(self):
        catalog = Catalog()
        catalog.add_item("ItemA", 10.99)
        # Assert that the item was added correctly
        self.assertEqual(catalog.get_catalog(), {"ItemA": 10.99})

    # Test case to check if an item can be removed from the catalog
    def test_remove_item_from_catalog(self):
        catalog = Catalog()
        catalog.add_item("ItemA", 10.99)
        catalog.remove_item("ItemA")
        # Assert that the item was removed correctly
        self.assertEqual(catalog.get_catalog(), {})

# This block ensures that the unit tests will be run when the script is executed
if __name__ == '__main__':
    unittest.main()
