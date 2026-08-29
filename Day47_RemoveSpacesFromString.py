string = input("Enter the string: ")
result = ""

for char in string:
    if char != ' ':
        result += char
print("After removing spaces:", result)
