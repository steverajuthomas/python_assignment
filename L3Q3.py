import os
filepath = os.path.abspath("words.txt")

string=""
with open(filepath,"r") as file:
    for line in file:
        for char in line:
            if char in ["j","J"]:
                string += "i"
            else:
                string+=char

print(string)
