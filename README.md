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