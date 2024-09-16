import os
file_path = os.path.abspath('doc.txt')

even_string_list=[]
with open(file_path, 'r') as file:
    for line in file:
        words=line.split()
        for word in words:
            if len(word)%2==0:
                even_string_list.append(word)
    print(even_string_list)
