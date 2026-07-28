n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
sum_of_elements = 0
for element in arr:
    sum_of_elements += element
average = sum_of_elements / n
print("Average of array elements =", average)
