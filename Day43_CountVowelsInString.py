string=input("enter the string:")
count=0;
for char in string:
    if char in "aeiouAEIOU":
        count=count+1
print("Vowel count is:",count)
