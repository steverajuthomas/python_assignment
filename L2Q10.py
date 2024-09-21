#The first pile has n stones. If n is
#even, then all piles have an even number of stones. If n is odd, all
#piles have an odd number of stones


# check if n is odd or even , incase it is odd, then you need to make with even steps and get to or as close to n
# if it is even, then you need to take odd steps and get to it or as close to n

n = 8
pile_list=[]

#even pile
if n%2==0:
    for i in range(1,n,2):
        pile_list.append(i)

else:
    for i in range(2, n, 2):
        pile_list.append(i)
print(pile_list)