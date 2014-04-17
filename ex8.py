#####Rock Paper Scissors
#Rock beats scissors
#Scissors beats paper
#Paper beats rock
import sys

user1 = raw_input("What is your name?")
user2 = raw_input("May I know your name too")
#print user1
#print user2

user1_choice = raw_input("%s, Do you want to choose rock, paper, or scissor" % user1)
user2_choice = raw_input("%s, Do you want to choose rock, paper, or scissor" % user2)
#print user1_choice
#print user2_choice

def compare(user1_choice, user2_choice):
    if user1_choice == user2_choice:
        return("It's a tie")
    elif user1_choice == 'rock':
        if user2_choice == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif user1_choice == 'scissors':
        if user2_choice == 'paper':
            return("Scissors wins!")
        else:
            return("Rock wins!")    
    elif user1_choice == 'paper':
        if user2_choice == 'rock':
            return("Paper wins!")
        else:
            return("Scissors wins!")    
    else:
         return("Invalid input! You have not entered Rock, Paper, or Scissors!")
         sys.exit()

print(compare(user1_choice, user2_choice))
