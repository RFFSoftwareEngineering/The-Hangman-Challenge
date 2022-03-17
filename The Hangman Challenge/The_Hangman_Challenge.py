# The hangman challenge, got challenged by a person, let's do it!
import random

word_book =["banana"]

chosen_word = random.choice(word_book)

size_chosen = len(chosen_word)

chosen_word_fixed = chosen_word.upper()

chosen_list = list(chosen_word_fixed)

enum_word = enumerate(chosen_word_fixed)

index = 0

restam = size_chosen

hits = chosen_list.copy()

hits_fixed = []
for item in hits:
    hits_fixed.append("_")

while restam > 0:

    x = input("chute uma letra\n")
    x = x.upper()

    if x in chosen_list:
        for index, item in enum_word:
            if x == item:
                print(f"você acertou a letra: {x} na pos {index}")
            else:
                print("x")
    else:
        restam -= 1
        print(f"você errou, restam {restam} erros")
