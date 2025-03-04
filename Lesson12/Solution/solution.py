import json
with open("text.txt", "r") as file:
    text = file.read()
    length = text
print(length)
str1 = ""
for i in text:
    str1 += chr(ord(i) + 3)

print("Koding :", str1)

str2 = ""
for i in str1:
    str2 += chr(ord(i) - 3)

print("DeKoding :", str2)

with open("text2.txt", "w") as file:
    file.write(str2)





