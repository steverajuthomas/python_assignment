#Write a Python program to find the common elements between two lists
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

l3=[]
for num in l1:
    if num in l2:
        l3.append(num)
print(l3)