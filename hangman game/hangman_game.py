import random
import hangman_stage
import word_file
# word_list = ["apple",'beautiful','potato']
lives = 6
choice_word = random.choice(word_file.words)
print(choice_word)
display = []
for i in range(len(choice_word)): # 0 1 2 3 4 5 #apple
               display += '_'
print(display)
game_over = False
while not game_over:
               guessed_letter = input("Gucess a Letter: ").lower() #r
               for positoin in range(len(choice_word)): #0 1 2 3 4
                 letter = choice_word[positoin]
                 if letter == guessed_letter:
                             display[positoin] = guessed_letter
               print(display)

               if guessed_letter not in choice_word:
                       lives -=1
                       if lives == 0:
                               game_over = True
                               print("You Lose!!")
               if '_' not in display:
                        game_over = True
                        print("You Win!!")
               print(hangman_stage.stages[lives])
                       



        

