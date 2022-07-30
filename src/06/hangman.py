
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


def cipher(new_character: list, word_in_list: str, key_searched: int) -> int:
    in_word = 0
    count = 0
    flag = 0
    print("Input a letter: ")
    letter = input()
    length_of_random_word = len(new_character)
    for i in range(length_of_random_word):
        if letter == new_character[i]:
            flag = 2
        elif letter == word_in_list[i]:
            new_character[i] = letter
            flag = 1
    new_character = "".join(new_character)
    in_word = new_character.count(letter)
    print(type(in_word))
    key_searched += in_word
    print(type(key_searched))
    print("SEEE Here my friend", new_character.count(letter))
    if flag == 1:
        print(new_character)
        count += 0
        if key_searched == len(new_character):
            count = 8
            print(new_character)
            print("You guessed the word!")
            print("You survived!")
    elif flag == 2:
        print(new_character)
        count += 1
        print("No improvements.")
        if key_searched == len(new_character):
            count = 8
            print(new_character)
            print("You guessed the word!")
            print("You survived!")
    else:
        print("That letter doesn't appear in the word")
        print()
        print(new_character)
        count += 1
    print("TSHI IS A KEY_SEARCHED:  {}".format(key_searched))
    return count


count = 0
key_searched = 0
word_in_list = get_word(words_game)
new_character = cipher_word(word_in_list)
print()
print(new_character)
new_character = list(new_character)
while count != 8:
    count = cipher(new_character, word_in_list, key_searched)
else:
    print("No improvements.")
    print()
    print("You lost!")





