s=input("enter the string:")
i=0
while i<len(s):
    c=0
    if s[i]>='0' and s[i]<='9':
        n=ord(s[i])-48
        for j in range(1,n+1):
            if n%j==0:
                c+=1
        if c==2:
            s=s[:i]+s[i+1:]
            i-=1
    i+=1
print("After deletion:",s)
