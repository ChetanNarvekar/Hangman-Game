
import random

import art
from words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# print(chosen_word)
end_of_game = False
lives = 6

from art import logo
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print(display)

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        print(art.stages[lives])
        if lives == 0:
            print("You Lose the game , better luck next time..")
            end_of_game = True
    if display == list(chosen_word):
        print("You won the game")
        break