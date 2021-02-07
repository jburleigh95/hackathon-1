def calculate_tax(total, tax_rate):
    pretax = total / (1 + tax_rate)
    tax_price = total - pretax
    print(f"Subtotal: ${pretax}")
    print(f"Tax:      ${tax_price}")


print("Calculate the price of an item before tax and the tax amount")
total_price = float(input("Enter the total price of the item: $"))
tax_rate = float(input("Enter the tax rate as a decimal: "))
calculate_tax(total_price, tax_rate)
