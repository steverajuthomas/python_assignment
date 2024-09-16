#Given an array of size N. The task is to rotate array by D elements towards right
arr = [1, 2, 3, 4, 5]
D = 2

solution_arr=[]

while D!=0:
    solution_arr.append(arr.pop())
    D-=1


for num in range(0,len(arr)-D):
    solution_arr.append(arr[num])

print(solution_arr)