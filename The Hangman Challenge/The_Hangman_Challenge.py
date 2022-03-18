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

    print(hits_fixed)

    index = 0

    x = input("chute uma letra\n")
    x = x.upper()

    if x in chosen_list:
        for item in chosen_list:
            if x == item:
                print(f"você acertou a letra: {x} no index {index}")
                hits_fixed.insert(index, x)
                hits_fixed.pop(index + 1)
                index += 1
            else:
                print("x")
                index += 1
    
    else:
        restam -= 1
        print(f"você errou, restam {restam} erros")

    if hits_fixed == chosen_list:
        print(hits_fixed)
        print("Parabéns! Você venceu!")
        restam = 0
