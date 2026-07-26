n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
print("Largest element =", largest)
