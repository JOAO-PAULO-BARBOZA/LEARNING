word = input("Type the word one: ")
word = word.lower()
word2 = input("Type the word two: ")
word2 = word2.lower()
if sorted(word) == sorted(word2):
    print("They're anagrams!")
else:
    print("They aren't anagrams!")

