n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
sum_of_elements = 0
for i in arr:
    sum_of_elements += i
print("Sum of array elements =", sum_of_elements)
