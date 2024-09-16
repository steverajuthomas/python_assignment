#Write a Python program to check if a given number is a perfect number

number=5
sum=0

for i in range(1,number):
    if number%i==0:
        sum+=i

if number==sum:
    print("Yes, perfect number")
else:
    print("No")
