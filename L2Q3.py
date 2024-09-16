#Given an array of N integers and an integer K, find the number of
#pairs of elements in the array whose sum is equal to K

arr = [1, 2, 3, 4, 5]
k = 6
pair_count=0
for num1 in range(len(arr)):
    for num2 in range(num1+1,len(arr)):
        if arr[num1]+arr[num2]==k:
            pair_count+=1

print(pair_count)
