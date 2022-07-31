import random

words_game = ['python', 'java', 'swift', 'javascript']
stages = {'play', 'results', 'exit'}
key_searched = 0
user_letters = ""
won = 0
lost = 0


def check_input(word: list) -> str:
    while True:
        user_answer = input()
        if user_answer.isascii() and len(user_answer) == 1:
            if user_answer.islower():
                return user_answer
            else:
                print("".join(word))
                print("Input a letter: ")
                print("Please, enter a lowercase letter from the English alphabet.")
        else:
            print("".join(word))
            print("Input a letter: ")
            print("Please, input a single letter.")


def get_word(a_list: list) -> str:
    random_word = random.randint(0, len(a_list) - 1)
    a_list = a_list[random_word]
    return a_list


def cipher_word(a_list: str) -> str:
    length_of_random_word = len(a_list)
    character_word = '-' * length_of_random_word
    return character_word


def start():
    global lost
    count = 0
    word_in_list = get_word(words_game)
    new_character = cipher_word(word_in_list)
    print()
    print(new_character)
    new_character = list(new_character)
    while count < 8:
        count += cipher(new_character, word_in_list)
    else:
        if count == 8:
            print()
            print("You lost!")
            lost += 1


def cipher(characer_new: list, a_list: str) -> int:
    global key_searched
    global user_letters
    global won
    count_of = 0
    flag = 0
    print("Input a letter: ")
    letter = check_input(characer_new)
    length_of_random_word = len(characer_new)
    for i in range(length_of_random_word):
        if letter in user_letters:
            flag = 2
        elif letter == a_list[i]:
            characer_new[i] = letter
            flag = 1
    characer_new = "".join(characer_new)
    in_word = characer_new.count(letter)

    if flag == 1:
        key_searched += in_word
        print(characer_new)
        if key_searched == len(characer_new):
            won += 1
            count_of = 10
            print(f"You guessed the word {characer_new}!")
            print("You survived!")
    elif flag == 2:
        print(characer_new)
        print("You've already guessed this letter.")
    else:
        print("That letter doesn't appear in the word")
        print()
        print(characer_new)
        count_of += 1

    user_letters += letter
    return count_of


def menu() -> None:
    global key_searched
    global user_letters
    while True:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit')
        user_begin = input()
        if user_begin not in stages:
            menu()
        elif user_begin == 'play':
            key_searched = 0
            user_letters = ""
            start()
        elif user_begin == "results":
            print(f'You won: {won} times.')
            print(f'You lost: {lost} times.')
        else:
            break


if __name__ == "__main__":
    print("H A N G M A N")
    menu()
