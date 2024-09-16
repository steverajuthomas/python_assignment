#Write a Python program to check if a string is an anagram of another string.
string1 = "listen"
string2 = "silent"

count=0

for i in string1:
    if i in string2:
        count+=1

if len(string1) == count:
    print("True")
else:
    print("False")