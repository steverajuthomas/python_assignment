#Write a Python program to create a list of given strings individually of the list using the Python map function.

#['Red', 'Blue', 'Black', 'White', 'Pink']
#[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i','n', 'k']]
#map(function, iterable)


def split_character(word):
    char_list=[]
    for char in word:
        char_list.append(char)
    return char_list

input_list=['Red', 'Blue', 'Black', 'White', 'Pink']

string_list=map(split_character,input_list)

print(list(string_list))


