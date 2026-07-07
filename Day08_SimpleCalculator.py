num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))
if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid Operator")
