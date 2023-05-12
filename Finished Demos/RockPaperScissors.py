# Write a rock, paper, scissors game
# import random module
import random
# define main function that handles all the logic
def main():
    # create a list of choices
    choices = ['rock', 'paper', 'scissors']
    # create a variable to control the loop
    again = 'y'
    # create a while loop to control the game
    while again == 'y' or again == 'Y':
        # get the user's choice
        user_choice = input('Enter rock, paper, or scissors: ')
        # get the computer's choice
        computer_choice = random.choice(choices)
        # determine the winner
        winner = determine_winner(user_choice, computer_choice)
        # display the results
        print('You chose', user_choice)
        print('The computer chose', computer_choice)
        print('The winner is', winner)
        # do this again?
        again = input('Do you want to play again? (y = yes): ')
# define the determine_winner function
def determine_winner(user, computer):
    # rock beats scissors
    if user == 'rock' and computer == 'scissors':
        return 'user'
    # paper beats rock
    elif user == 'paper' and computer == 'rock':
        return 'user'
    # scissors beats paper
    elif user == 'scissors' and computer == 'paper':
        return 'user'
    # computer wins
    else:
        return 'computer'
# call the main function
main()
