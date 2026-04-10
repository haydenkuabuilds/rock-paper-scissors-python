#all the imports
import random
import winsound

while True:

#randomiser for selecting options
    cpu=random.randint(1, 3)
    if cpu==1:
        option=("rock")
    elif cpu==2:
        option=("paper")
    else:
        option=("scissors")

    user_move = input(str("Rock, Paper, Scissors... Shoot! (type rock, paper, or scissors): ")).lower()
    
    
    if user_move=="rock":
       print(f"You chose Rock! I chose {option}!")
       winsound.Beep(1000, 500)
        
    elif user_move=="paper":
        print(f"You chose Paper! I chose {option}!")
        winsound.Beep(1000, 500)
        
    elif user_move=="scissors":
        print(f"You chose Scissors! I chose {option}!")
        winsound.Beep(1000, 500)
        
    else:
        print("That doesnt exist. Try again!")
        winsound.Beep(1000, 500)
        winsound.Beep(1000, 500)
        
        continue


    if user_move == option:
        print ("It's A Draw!")
    elif user_move=="paper" and option=="scissors":
        print ("You  Lost! Lets another round!")
    elif user_move=="paper" and option=="rock":
        print ("You Won! Lets play another round!")
    elif user_move=="scissors" and option=="paper":
        print ("You Won! Lets play another round!")
    elif user_move=="scissors" and option=="rock":
        print ("You Lost! Lets play another round!")
    elif user_move=="rock" and option=="scissors":
        print ("You Won! Lets play another round!")
    elif user_move=="rock" and option=="paper":
        print ("You lost! Lets play another round!")

