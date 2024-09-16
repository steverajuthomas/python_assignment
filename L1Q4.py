#Write a Python program to find the sum of all odd numbers between two given numbers
Start = 1
stop = 10

sum=0

for number in range(Start,stop+1):
    if number%2!=0:
        sum+=number
print(f"Sum of all odd numbers between {Start} and {stop} are {sum}")