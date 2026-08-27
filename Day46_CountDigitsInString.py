string=input("Enter a string:")
d=0;
for char in string:
    if '0'<=char<='9':
        d+=1
print("Number of digits:",d)
