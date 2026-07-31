n1 = int(input("Enter the number of elements in first list: "))
print(f"Enter {n1} elements:")
list1 = list(map(int, input().split()))
n2 = int(input("Enter the number of elements in second list: "))
print(f"Enter {n2} elements:")
list2 = list(map(int, input().split()))
merged_list = []
for i in range(n1):
    merged_list.append(list1[i])
for i in range(n2):
    merged_list.append(list2[i])
print("First List  :", list1)
print("Second List :", list2)
print("Merged List :", merged_list)
