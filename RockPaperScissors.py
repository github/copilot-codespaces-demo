# Write a rock, paper, scissors game  
# import random module
import random
# define main function that handles all the logic
def main():
    # define variables
    # rock = 1, paper = 2, scissors = 3
    rock = 1
    paper = 2
    scissors = 3
    # get user input
    user = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
    # generate random number for computer
    computer = random.randint(1,3)
    # determine winner
    # rock beats scissors
    if user == rock and computer == scissors:
        print("You win! Rock beats scissors!")
    # paper beats rock
    elif user == paper and computer == rock:
        print("You win! Paper beats rock!")
    # scissors beats paper
    elif user == scissors and computer == paper:
        print("You win! Scissors beats paper!")
    # tie
    elif user == computer:
        print("It's a tie!")
    # computer wins
    else:
        print("Computer wins!")

# call main function
main()




    




    