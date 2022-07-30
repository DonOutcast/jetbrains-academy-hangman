
import random

print("H A N G M A N")

words_game = ['python', 'java', 'swift', 'javascript']


def get_word(words_game: list) -> str:
    random_word = random.randint(0, len(words_game) - 1)
    word_in_list = words_game[random_word]
    return word_in_list


def cipher_word(word_in_list: str) -> str:
    length_of_random_word = len(word_in_list)
    new_character = '-' * length_of_random_word
    return new_character


def cipher(new_character: str, word_in_list: str) -> None:
    flag = 0
    print("Input a letter: ")
    letter = input()
    length_of_random_word = len(new_character)
    for i in range(length_of_random_word):
        if letter == word_in_list[i]:
            new_character[i] = letter
            flag = 1
    new_character = "".join(new_character)
    if flag == 1:
        print(new_character)
    else:
        print("That letter doesn't appear in the word")
        print()
        print(new_character)

count = 0
word_in_list = get_word(words_game)
new_character = cipher_word(word_in_list)
print()
print(new_character)
new_character = list(new_character)
while count != 8:
    cipher(new_character, word_in_list)
    count += 1
else:
    print("Thanks for playing!")


