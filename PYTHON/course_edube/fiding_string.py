from random import randint

random_word = ""
alphabeta = "abcdefghijklmnopqrstuvxywz"
for i in range(15):
    random_word += alphabeta[randint(0, len(alphabeta))]
print(random_word)

wr = input("Type a word: ")


