import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

randomPhrase

characters = [each_character.rstrip('') for each_character in randomPhrase]
characters.reverse()
reversePhrase = ''.join(characters[i] for i in range(len(characters)))
    
print(reversePhrase)