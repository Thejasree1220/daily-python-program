num = input("Enter a number: ")
product = 1
for digit in num:
    product *= int(digit)
print("Product of digits =", product)
