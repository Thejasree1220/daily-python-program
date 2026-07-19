num = int(input("Enter a number: "))
original_num = num
sum_of_factorials = 0
while num > 0:
    digit = num % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum_of_factorials += factorial
    num //= 10
if sum_of_factorials == original_num:
    print(original_num, "is a Strong Number.")
else:
    print(original_num, "is not a Strong Number.")
