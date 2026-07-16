start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers are:")

for num in range(start, end + 1):
    prime = 0

    for i in range(1, num):
        if num % i == 0:
            prime=prime+1

    if prime==2:
        print(num, end=" ")
