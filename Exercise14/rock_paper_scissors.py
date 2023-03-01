# function to ask user for input


def user_choice():
    options = ['R', 'P', 'S']
    user = input("Choose 'R' for Rock, 'P' for Paper or 'S' for Scissors: ")
    while user.upper() not in options:
        print("That is not an option, please try again..")
        user = input("Choose 'R' for Rock, 'P' for Paper or 'S' for Scissors: ")
    return user


# function to change to Rock, Paper, Scissor


def change_user(user_rps):
     if user_rps.upper()=='R':
         user_rps = 'Rock'
         return user_rps
     elif user_rps.upper()=='P':
         user_rps = 'Paper'
         return user_rps
     elif user_rps.upper()=='S':
         user_rps = 'Scissors'
         return user_rps


import random
# function to generate random number between 0 and 2


def random_number():
     rand_num = random.randint(0,2)
     return rand_num


# function to change number to a choice


def change_comp(comp_choice):
     if comp_choice == '0':
         comp_word ='Rock'
         return comp_word
     elif comp_choice == '1':
         comp_word = 'Paper'
         return comp_word
     elif comp_choice == '2':
         comp_word = 'Scissors'
         return comp_word


# define a function to indicate winner


def result(word1, word2):
    if word1 == word2:
        final = 'Draw'
        return final
    if word1 == 'Rock':
        if word2 == 'Paper':
            final = 'You lose'
            return final
        if word2 == 'Scissors':
            final = 'You win'
            return final
    if word1 == 'Paper':
        if word2 == 'Rock':
            final = 'You win'
            return final
        if word2 == 'Scissors':
            final = 'You lose'
            return final
    if word1 == 'Scissors':
        if word2 == 'Rock':
            final = 'You lose'
            return final
        if word2 == 'Paper':
            final = 'You win'
            return final


# ask user for input
# user_choice()
user_rps = user_choice()

# change to rock, paper, scissors
word1 = change_user(user_rps)
print("Your choice: ", word1)

# generate random number between 0 and 2
comp_choice = str(random_number())

# change number to a word
word2=change_comp(comp_choice)
print("Computer choice: ", word2)

# decide the winner
decision = result(word1,word2)
print(decision)