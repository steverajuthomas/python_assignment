#Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number
#Sample Input: num = 987
#Sample Output: Sum_of_digits = 24
#6

input_number=987
sum_digits=0

while len(str(input_number))>1:
    sum_digits=0
    while input_number>0:
        digit=input_number%10
        sum_digits+=digit
        input_number=input_number//10
    input_number=sum_digits

print(sum_digits)