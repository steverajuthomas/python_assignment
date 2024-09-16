#Write a Python program to reverse a number using a while loop

num = 12345
solution_string=""
while num>0:
    digit=num%10
    solution_string+=str(digit)
    num = num//10
print(solution_string)
