# The hangman challenge, got challenged by a person, let's do it!
import random

word_book =["Viking Code", "banana", "ownado", "cara bobo"]

chosen_word = random.choice(word_book)

size_chosen = len(chosen_word)

chosen_word_fixed = chosen_word.upper()

trys = 0

while trys < size_chosen:
    x = input("digite sair para sair para desistir\nChute uma letra!\n")
    if x == "sair":
        break
    trys += 1

print("Game Over!")
