#Make sure to ask for a Re-Type Password and if the
#password is incorrect give a chance to enter it again but it should
#not be more than 3 times

counter=1
while counter<=3:
    username=input("Enter username : ")
    password=input("Enter password: ")

    user_info_dict={'tom':'cat','jerry':'mouse','randy':'dog','tweety':'pigeon'}

    for key,value in user_info_dict.items():
        if key == username and value==password:
            print("user logged in sucessfully")
            exit()

    print("incorrect username or password. Try again")
    counter+=1
