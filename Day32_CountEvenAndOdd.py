n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements:")
arr = list(map(int, input().split()))
even_count = 0
odd_count = 0
for i in range(n):
    if arr[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even elements count =", even_count)
print("Odd elements count =", odd_count)
