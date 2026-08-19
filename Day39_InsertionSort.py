n=int(input("Enter the number of elements:"))
print(f"Enter {n} elements:")
arr=list(map(int,input().split()))
for i in range(1,n):
    key=arr[i]
    j=i-1
while j>=0 and arr[j]>key:
    arr[j+1]=arr[j]
    j=j-1
    arr[j+1]=key
print("Sorted List:",end=" ")
for i in range(n):
    print(arr[i],end=" ")
print(end="\n")
