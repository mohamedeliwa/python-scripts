import random
import sys


words = []
letters = []

'''taking words list from user'''
while True:
    word = input("Enter a word: ")
    if word == '' and len(words) == 0:
        sys.exit()
    elif word == '':
        break
    else:
        words.append(word)

# spliting words list into letters
for word in words:
    for letter in word:
        letters.append(letter)

random.shuffle(letters)

# generating 10 words randomly
for _ in range(10):
    shuffled_word = []
    for _ in range(5):
        index = random.randint(0, len(letters)-1)
        shuffled_word.append(letters[index])
    print("".join(shuffled_word))


'''generating random words from a list of words provided by the user'''
''' This script needs to be improved to generate better words'''