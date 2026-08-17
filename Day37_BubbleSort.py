n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted list:", end=" ")
for i in range(n):
    print(arr[i], end=" ")
