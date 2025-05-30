import calculator
import shopping

cal = calculator.Calculator()

print("Calculator Test Cases: ")
print("7 + 5 =", cal.add(7, 5)) #test case 1
print("34 - 21 =", cal.sub(34, 21)) #test case 2
print("54 * 2 =", cal.mul(54, 2)) #test case 3
print("144 / 2 =", cal.div(144, 2)) #test case 4
print("45 / 0 =", cal.div(45, 0)) #test case 5


cart = shopping.Cart()

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
