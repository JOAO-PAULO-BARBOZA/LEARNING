#MIRRORING WORDS
word = input('Type the word to be mirrored :')
list_word = list(word)
mirrored_list = []
for i in range(len(word)):
    mirrored_list.extend(list_word.pop())
mirrored_word = ''.join(mirrored_list)
print (mirrored_word)

