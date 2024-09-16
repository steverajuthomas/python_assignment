#Write a Python program that executes an operation on a list and
#handles an IndexError exception if the index is out of range


try:
    num_list=[10,14,16,14,21,21]
    count_of_repeated_numbers=0
    for num1 in range(0,len(num_list)):
        for num2 in range(num1+1,len(num_list)):
            if num_list[num1]==num_list[num2]:
                count_of_repeated_numbers+=1
    print(f"Number of numbers repeated in the list are {count_of_repeated_numbers}")
except IndexError as e:
    print(f"out of index error occured: {e}")