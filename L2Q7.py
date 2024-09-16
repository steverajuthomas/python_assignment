#Write a Python function that finds the median of a list of numbers.

number_list=[7, 2, 5, 1, 9, 3]
number_list.sort()
middle_element_index=(len(number_list)-1)//2


if len(number_list)%2==0:
    median=(number_list[middle_element_index]+number_list[middle_element_index+1])/2
else:
    median=number_list[middle_element_index]

print(median)
