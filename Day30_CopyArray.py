n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements:")
arr1 = list(map(int, input().split()))
arr2 = []
for i in range(n):
    arr2.append(arr1[i])
print("Original List :", arr1)
print("Copied List   :", arr2)
