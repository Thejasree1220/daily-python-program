num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is the largest.")
elif num2 > num1:
    print(num2, "is the largest.")
else:
    print("Both numbers are equal.")
