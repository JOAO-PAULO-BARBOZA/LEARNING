word = input("Type a word/phase and look out if it's a palindrome: ")
word = word.replace(" ", "").lower()
check = word[len(word)::-1]

if len(word) == 0:
    print("It's not a palindrome!")
elif check == word:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")


