#Write a Python function that counts the number of vowels in a given string
input_string = "Hello, World!"

vowels_string="aeiouAEIOU"
counter=0
for char in input_string:
    if char in vowels_string:
        counter+=1

print(f"The number of vowels in string are {counter}")