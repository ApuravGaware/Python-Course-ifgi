import easy_shopping

cart = easy_shopping.shopping.Cart()
# Adding things cart
cart.add_item("Apfel", 10)
cart.add_item("Eier", 18)
cart.add_item("Brot", 20)

# Show cart
print("\nItems in Shopping Cart:", cart.show_cart())
print("Total Quantity:", cart.quantity())

# Remove 1 thing from cart & showing cart again
cart.remove_item("Brot")
print("\nUpdated Cart after 1 removal:", cart.show_cart())
print("Total Quantity:", cart.quantity()) 
