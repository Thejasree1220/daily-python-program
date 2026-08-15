n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
largest = arr[0]
second_largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]
print("Second largest element =", second_largest)
