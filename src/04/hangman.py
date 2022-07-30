import random

print("H A N G M A N")

words_game = ['python', 'java', 'swift', 'javascript']
random_word = random.randint(0, len(words_game) - 1)
word_in_list = words_game[random_word]
length_of_random_word = len(word_in_list)
position = 3
count = length_of_random_word - position
new_character = '-' * count
some_word = word_in_list[:position] + new_character

print(f"Guess the word {some_word}: ")
word = input()
while True:
    if word == words_game[random_word]:
        print("You survived!")
        break
    print("You lost!")
    break

