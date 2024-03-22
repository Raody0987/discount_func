def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Get user input

original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount)

print(f"The final price after applying the discount is: ${final_price}")




