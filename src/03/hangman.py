import random

print("H A N G M A N")
print("Guess the word: ")
words_game = ['python', 'java', 'swift', 'javascript']
random_word = random.randint(0, len(words_game) - 1)


word = input()
while True:
    if word == words_game[random_word]:
        print("You survived!")
        break
    print("You lost!")
    break
