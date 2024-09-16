#lambda function
input_string = "Hello, World!"
given_char = "H"

flag = lambda input_string,given_char:True if given_char in input_string else False

print(flag(input_string,given_char))
