n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
print("Original array:", arr)
reversed_array = []
for i in range(n - 1, -1, -1):
    reversed_array.append(arr[i])
print("Reversed array:", reversed_array)
