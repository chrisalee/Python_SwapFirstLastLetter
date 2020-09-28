sentence = ""
words = "look at all these random words"
word_list = words.split(" ")
for i in range(len(word_list)):
    word = word_list[i]
    first_letter = word[0]
    middle = word[1:len(word)-1]
    last_letter = word[len(word)-1]
    sentence = sentence + " " + last_letter + middle + first_letter
print(sentence)