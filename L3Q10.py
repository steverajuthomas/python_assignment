# You are given an integer N representing the number of computers in the cafe and a sequence of uppercase letters S.
# Every letter in S occurs exactly two times. The first occurrence denotes the arrival of a customer and
# the second occurrence denotes the departure of the same customer if he gets allocated the computer.
# You have to find the number of customers that walked away without using a computer.

# Input:
# N = 3
# S = GACCBDDBAGEE
# Output: 1
# Explanation: Only D will not be able to get any computer. So the
# answer is 1.
##########################################################
# dict values ->0 - first time customer, 1- computer occupied , 2 - customer leaving
N = 3
S = 'GACCBDDBAGEE'
customer_dict={}
customer_without_computer=0

for customer in S:
    if customer not in customer_dict:
        customer_dict[customer]=0

    if customer_dict[customer]==0:
        if N>0:
            N-=1
            customer_dict[customer]=1
        else:
            customer_without_computer+=1
            customer_dict[customer] = 2

    elif customer_dict[customer]==1:
        N+=1
        customer_dict[customer] == 2

print(customer_without_computer)




