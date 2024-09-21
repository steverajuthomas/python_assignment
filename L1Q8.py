#Write a Python program to calculate the LCM (Least Common Multiple) of two numbers
number1 = 12
number2 = 18

larger_number=max(number1,number2)

while True:
    if (larger_number%number1)==0 and (larger_number%number2)==0:
        LCM=larger_number
        break
    larger_number+=1

print(LCM)



