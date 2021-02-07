str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) < len(str2):
    max_len = len(str1)
else:
    max_len = len(str2)

new_str1 = ""
new_str2 = ""
for char in range(max_len):
    if char % 2 == 0:
        new_str1 += str1[char]
        new_str2 += str2[char]
    else:
        new_str1 += str2[char]
        new_str2 += str1[char]

print(new_str1)
print(new_str2)
