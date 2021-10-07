word_without_vowels = ""
user_word = input("Type a word: ")
user_word = user_word.upper()
for letter in user_word:
    if letter in 'AEIOU':
        continue
    else: word_without_vowels = word_without_vowels + letter
print(word_without_vowels)

