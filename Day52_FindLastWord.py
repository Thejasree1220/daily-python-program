s = input("enter the string: ")
i = 0
p = 0
while i < len(s):
    if s[i] == ' ':
        p = i + 1
    i += 1
q = i - 1
print("last word:", end=" ")
while p <= q:
    print(s[p], end="")
    p += 1
print()
