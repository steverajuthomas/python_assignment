#Write a program that accepts a string as input from the user and calculates the number of digits and letters

user_input = input("Enter your word here ")

letters="abcdefghijklmnopqrsutvwxyz"
digits="0123456789"
letter_count=0
digits_count=0

for char in user_input:
    if char in letters:
        letter_count+=1
    elif char in digits:
        digits_count+=1
        
print(f"Alphabets:{letter_count} & Number:{digits_count}")