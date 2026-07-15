num = int(input("Enter a positive integer: "))
prime = 0
for i in range(2, num):
     if num % i == 0:
            prime=prime+1;
if prime==2:
    print(num, "is a Prime Number.")
else:
    print(num, "is not a Prime Number.")
