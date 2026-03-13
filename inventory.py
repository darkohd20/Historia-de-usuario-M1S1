
# Ask the user for the product name
name = input("enter the name: ")

# validate if the name is spelled correctly
while name.isalpha() == 0:
    print("The name cannot be empty. Try again.")
    name= input("enter the name: ")

# Ask the user for the product price and validate it is a decimal number
price = 0
while price <= 0:
    try:
        price = float(input("enter the price: "))
        
        if price <=0:
            print("el numero que ingreso no es valido, por favor ingrese nuevamente el precio")
            continue

        break
    except ValueError:
        print("Invalid price. enter a number (ex: 10.00).")

# Ask the user for the product amount and validate it is a whole number
amount = 0
while amount <= 0:
    try:
        amount = int(input("enter the amount: "))
        
        if amount <=0:
            print("el numero que ingreso no es valido, por favor ingrese nuevamente el precio")
            continue

        break
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
