import random
user_choice = int(input("Enter your Choice: Type 0 for Rock, 1 for Paper,,2 for scissor. "))
if  user_choice >=3 or user_choice < 0:
               print("You entered invalid number,You loss.")
else:
        computer_choices = random.randint(0,2)
        print("Computer Choice:")
        print(computer_choices)
        if computer_choices == user_choice:
                print("It's Draw")
        elif computer_choices == 0 and user_choice == 2:
                print("You loss")
        elif user_choice==0 and computer_choices == 2:
                print("You win")
        elif computer_choices > user_choice: #2 > 0
                print("You Loss.")
        elif user_choice > computer_choices: #2 > 0
                print("You win.")

        
