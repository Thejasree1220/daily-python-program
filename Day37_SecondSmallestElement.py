n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
smallest = arr[0]
second_smallest = None
for i in range(1, n):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i] != smallest and (second_smallest is None or arr[i] < second_smallest):
        second_smallest = arr[i]
print("Second smallest element =", second_smallest)
