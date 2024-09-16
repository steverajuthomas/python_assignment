#Create a function that takes a list and returns a new list with unique elements of the first list.
list1 = [1, 2, 2, 3, 4, 4, 5, 5]

list2=[]
for num in list1:
    if num not in list2:
        list2.append(num)
print(list2)