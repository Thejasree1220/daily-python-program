num = int(input("Enter an integer: "))
original_num = num
reverse = 0
while num != 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num //= 10
if original_num == reverse:
    print(original_num, "is a Palindrome Number.")
else:
    print(original_num, "is not a Palindrome Number.")
