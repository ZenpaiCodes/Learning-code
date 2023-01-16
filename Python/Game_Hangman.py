import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

 
import random
word_list = ["university", "colombia", "bogota", "house"]

random_word = random.choice(word_list)

# PLAYER guess
guess = input("Type a letter to see if it\'s part of the word? ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-4: - Create an empty List called display.
#TODO-4.1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
lives = 6
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)

#TODO-7: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while display[position] == "_":
    print(f"{lives} lives remaining\n")
    if lives == 0:
        print("You LOSE!")
        break
    guess = input("Type a letter to see if it\'s part of the word? ").lower()
    if guess not in chosen_word:
        lives = lives - 1
        print(stages[lives])
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)

if display[position] != "_":
        print("You WON!")
print(f"The word was: {chosen_word}")