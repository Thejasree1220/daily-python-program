s=input("enter the string:")
l=len(s)
c=0
for i in range(1,l+1):
    if l%i==0:
        c+=1
if c==2:
    print(l,"is prime")
else:
    print(l,"is not a prime")
