
# Ask the user for the product name
name = input("enter the name: ").strip()
# validate if the name is spelled correctly
while len(name) == 0:
    print("The name cannot be empty. Try again.")
    name = input("enter the name: ").strip()
# Ask the user for the product price and validate it is a decimal number
price = None
while price is None:
    try:
        price = float(input("enter the price: "))
    except ValueError:
        print("Invalid price. enter a number (ex: 10.00).")
# Ask the user for the product amount and validate it is a whole number
amount = None
while amount is None:
    try:
        amount = int(input("enter the amount: "))
    except ValueError:
        print("invalid amount. enter an amount (ex: 12, 30). ")
# Multiply price by amount to get the total cost
operation = (price * amount)
total_cost = operation
# # Display all the product information and the calculated total cost
print(f"Product name:", name, "/Unit price:", price, "/amount:", amount,"/Calculated total cost:", total_cost)
# This program asks the user for a product name, price and amount.
# It validates that the name is not empty, the price is a decimal number
# and the amount is a whole number, repeating the question if the input is invalid.
# Finally, it calculates and displays the total cost of the product.
