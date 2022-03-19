import random

word_book =["banana", "Viking Code", "Zica das Balada", "Professor Pardal", "computador", "imposto", "sucesso", "Comida", "Mina Louca", "etecetera", "macaco", "pudim", "Ovo Frito", "Novinha Safada", "Palavra"]

chosen_word = random.choice(word_book)

size_chosen = len(chosen_word)

chosen_word_fixed = chosen_word.upper()

chosen_list = list(chosen_word_fixed)

enum_word = enumerate(chosen_word_fixed)

index = 0

restam = 8
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
        print(f"você errou, restam {restam - 1} erros")

    if hits_fixed == chosen_list:
        print(f"""
                                    Parabéns você Venceu!                           
                                    ---------------------
                                  _ |                   | _                              
                                 ) )|                   |( (                               
                                 \ \|      Won!         |/ /                          
                                  ) )                   ( (                            
                                 / /|                   |\ \                                
                                 ) )|                   |( (                           
                                 |_|\                   /|_|                             
                                     \                 /                               
                                      -----------------                              
                                      )               (                              
                                      |_______________|                                
                                {hits_fixed}                                      
              """)  
        restam = 0

    elif restam == 7:
        print("""
                                    Você errou!              
                                    ______                                
                                   |      |                                     
                                   |                                        
                                   |
                                   |                                                   
                                  / \                                                      
              """)
    elif restam == 6:
        print("""
                                    Você errou!              
                                    ______                                
                                   |      |                                     
                                   |      O                                                            
                                   |
                                   |                                                   
                                  / \                                                      
              """)
    elif restam == 5:
        print("""
                                    Você errou!              
                                    ______                                
                                   |      |                                     
                                   |      O                                                             
                                   |      |                              
                                   |                                                   
                                  / \                                                      
              """)
    elif restam == 4:
        print("""
                                    Você errou!              
                                    ______                                
                                   |      |                                     
                                   |      O                                                             
                                   |      |                                 
                                   |     /                                                                                        
                                  / \                                                      
              """)
    elif restam == 3:
        print("""
                                    Você errou!              
                                    ______                                
                                   |      |                                     
                                   |      O                                                             
                                   |      |                                 
                                   |     / \                                                                           
                                  / \                                                      
              """)
    elif restam == 2:
        print("""
                                    Você errou!              
                                    ______                                
                                   |      |                                     
                                   |      O                                                             
                                   |      |-                                                                            
                                   |     / \                                                                           
                                  / \                                                      
              """)
    elif restam == 1:
        print("""
                                    Você errou!              
                                    ______                                
                                   |      |                                     
                                   |      O         game over                                                    
                                   |     -|-                                                                     
                                   |     / \                                                                           
                                  / \                                                      
              """)
        break
