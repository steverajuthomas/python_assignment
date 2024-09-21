Input = 'Robert000Smith000123'
# Output:{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

input_with_one_zero=''
for i in range(len(Input)):
    if Input[i]=='0' and Input[i+1]=='0':
        pass
    else:
        input_with_one_zero+=Input[i]

l1=input_with_one_zero.split('0')
l2=['first_name','last_name','id']

output_dict={l2[i]:l1[i] for i in range(len(l1))}

print(output_dict)