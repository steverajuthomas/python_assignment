#Write a Python program to reverse the order of words in a given sentence
Input_sentence = "Hello, World! Welcome to Python programming."
#Output after reverse = “programming. Python to Welcome World! Hello,”

words=Input_sentence.split()
#print(words)

reversed_word=""
for word in range(len(words)-1,-1,-1):
    reversed_word += words[word] + " "
    #print(words[word])

print(reversed_word)