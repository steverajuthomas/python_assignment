Input='wwwwaaadebbbbbw'
# Output: w4a3d1e1b5w1

counter=1
length_encoded_string=Input[0]
for i in range(len(Input)):
    if(i+1<len(Input)):
        if Input[i]==Input[i+1]:
            counter+=1
        else:
            length_encoded_string+=str(counter)
            counter=1
            length_encoded_string+=Input[i+1]
    else:
        length_encoded_string+=str(counter)

print(length_encoded_string)

