#Write a Python program to count the frequency of each element in a list.

Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
solution_dict={}

for element in Input_list:
    if element in solution_dict:
        solution_dict[element]+=1
    else:
        solution_dict[element]=1

print(solution_dict)