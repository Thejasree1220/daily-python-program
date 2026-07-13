num = int(input("Enter a 3-digit integer: "))
original_num = num
result = 0
while original_num != 0:
    remainder = original_num % 10
    result += remainder ** 3
    original_num //= 10
if result == num:
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")
