start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("Perfect Numbers are:")
for num in range(start, end + 1):
    if num < 2:
        continue
 sum_of_divisors = 0
for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == num:
        print(num)
