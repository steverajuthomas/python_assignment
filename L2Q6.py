#Write a Python program to check if a number is a power of two using recursion


def power_of_two(number):

    #base condition
    if number == 1:
        return True
    #recursive part
    elif number%2!=0:
        return False

    return power_of_two(number//2)

number =16
if power_of_two(number):
    print("number is a power of two")
else:
    print("number is not a power of two")


