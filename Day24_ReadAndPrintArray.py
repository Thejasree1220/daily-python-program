n = int(input("Enter the number of elements: "))
arr = []
print("Enter", n, "elements:")
for i in range(n):
    element = int(input())
    arr.append(element)
print("Array elements are:")
for element in arr:
    print(element, end=" ")
