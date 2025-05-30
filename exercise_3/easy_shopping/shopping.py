# Shopping.py for making a cart
class Cart:
    def __init__(self):
        self.items = {}

    # Add item
    def add_item(self, item_name, qty):
        if item_name in self.items:
            self.items[item_name] += qty
        else:
            self.items[item_name] = qty

    # Remove item 
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Item '{item_name}' not found in cart.")

    #show
    def show_cart(self):
        return self.items

    # total quantity of items
    def quantity(self):
        return sum(self.items.values())
