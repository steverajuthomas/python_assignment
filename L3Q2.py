import os
file_path = os.path.abspath('demo.txt')

line_count=0
with open(file_path,"r") as file:
    for line in file:
        line_count+=1
print(f"the number of lines in the file are {line_count}")
