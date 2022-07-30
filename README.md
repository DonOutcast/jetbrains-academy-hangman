# Hangman

## Description
Hangman is a popular, funny, yet very grim game. A cruel computer hides a word from you and you need to guess it, letter by letter. If you fail, you'll be hanged, if you win, you'll survive.

You're probably familiar with the rules; now you can create this game yourself!

Let's take a brief look at what you are going to build in this project. Here is what the gameplay will look like:

In the main menu, players can choose to either play or exit the game;
If players choose to play, the computer picks a word from a list — it will be the answer;
The computer asks players to enter a letter that may or may not be in the word;
If players suggest a letter that does not appear in the word for the first time, It's a miss. A player can miss 8 times before the game is over;
If the letter does occur in the word, the computer notifies the players. If there are letters left to guess, the computer invites the player to go on;
When the entire word is uncovered — it's a victory! The game should calculate the final score and return to the main menu.
This may sound complex, but the project is split into small stages with the hints that will guide you. We guarantee that the final product is replayable and quite engaging!

Let's start with an announcement that will greet the player. You already know how to print with Python. Apply that knowledge to entice your friends to play with an announcement for your game!

## Part 1 Hello.
In this stage, write a program that prints the lines shown in the example below.

### Example
Output:

H A N G M A N
The game will be available soon.

## Part 2 Let’s play a game.
### Description
In this stage, we will add some simple gameplay. There will be two possible outcomes. Let's first print a welcoming message and then ask players to guess the word we have set for the game. If they guess the word, the game reports a win; otherwise, it will "hang" the player.

### Objectives
Ask players for a possible word;
Print You survived! if users guess the word;
Print You lost! if users fail.
In this stage, python is the word that players need to guess. For now, this is the only form of answer that is deemed correct, so there is no need to worry about the register or punctuation marks.
### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

- Example 1:

H A N G M A N
Guess the word: > python
You survived!
- Example 2:

H A N G M A N
Guess the word: > java
You lost!
## Part 3 Make your choice.
### Description
If there is only one word, the game becomes dull. You already know the word, and there’s no challenge. In this stage, let's make the game more difficult by choosing a word from the special list with a variety of options. This way, our game gains in replayability.

### Objectives
Create the following list of words: python, java, swift, javascript;
Program the game to choose a word from the list at random (you can use the random library for that). You can enter more words, but let's stick to these four for now.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

- Example 1: computer chooses python from the list.

H A N G M A N
Guess the word: > python
You survived!
- Example 2: computer chooses something other than python from the list.

H A N G M A N
Guess the word: > python
You lost!
- Example 3: computer randomly chooses something other than swift from the list.

H A N G M A N
Guess the word: > swift
You lost!

## Part 4 Help is on the way
### Description
The game is now more difficult to beat; your chances of guessing the word depend on the list size. If there are four words in the list, you have a 25% chance. Let's show a little mercy and add hints for our players.

### Objectives
As in the previous stage, use the following word list: python, java, swift, javascript;
Once the computer has chosen a word from the list, show its first three letters. Replace the hidden letters with hyphens (-).
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

- Example 1:

H A N G M A N
Guess the word jav-: > java
You survived!
- Example 2:

H A N G M A N
Guess the word pyt---: > pythia
You lost!

## Part 5 Keep trying
Description
Let's make the game iterative. In this stage, we'll adjust our game to resemble the classic version of Hangman. Players should now guess the letters in a word instead of inputting an entire word. If an attempt is successful, uncover the letter. We also need to add the lose condition — players have eight attempts to guess all letters that appear in the word. When players run out of attempts, the game ends.

Don't forget to get rid of the hints: replace all the letters in a word with hyphens at the beginning. Players input one lowercase letter at a time, so there is no need to worry about that.

Later on, we will also determine the win conditions, but in this stage, let's just see how well our player guesses the word on each attempt.

Objectives
Your game should work as follows:

Players have exactly eight attempts to guess the word by entering letters one by one. Asking for a letter, print: Input a letter:. If a player uncovered all the letters, but some attempts are still left, the program must continue to ask for input until all the tries are exhausted;
If the letter doesn't appear in the word, the computer takes one try away – even if a user has already suggested this letter – and prints That letter doesn't appear in the word.;
If the letter does appear in the word but a user has already suggested this letter and it's open, no need to print any messages;
If all attempts are exhausted, the game ends; the program shows a final message (Thanks for playing!). Otherwise, players can continue to input letters;
We continue to stick with the word list from the previous stage: python, java, swift, javascript. It ensures that your program is tested reliably. Don't worry about javascript. Yes, it's longer than 8 characters, but we'll keep it in the list for consistency since we're not done with developing the game yet and for now there is no win or lose.
Please, make sure that the output format of your program follows the example precisely. Pay attention to the empty lines between attempts and at the end.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input. Comments after # provided for illustrative purposes and not as part of the task.

Example 1:

H A N G M A N  # 8 attempts

----------
Input a letter: > a  # 7 attempts

-a-a------
Input a letter: > i  # 6 attempts

-a-a---i--
Input a letter: > o
That letter doesn't appear in the word.  # 5 attempts

-a-a---i--
Input a letter: > z
That letter doesn't appear in the word.  # 4 attempts

-a-a---i--
Input a letter: > l
That letter doesn't appear in the word.  # 3 attempts

-a-a---i--
Input a letter: > p  # 2 attempts

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word.  # 1 attempt

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word.  # 0 attempts

Thanks for playing!
Example 2:

H A N G M A N  # 8 attempts

----
Input a letter: > j  # 7 attempts

j---
Input a letter: > i
That letter doesn't appear in the word.  # 6 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 5 attempts

j---
Input a letter: > o
That letter doesn't appear in the word.  # 4 attempts

j---
Input a letter: > a  # 3 attempts

ja-a
Input a letter: > v  # 2 attempts

java
Input a letter: > a  # 1 attempt

java
Input a letter: > j  # 0 attempts

Thanks for playing!