import random

computer = 0
you = 0

for i in range(5):
    randon_number = random.randint(0,2)

    if randon_number == 0:
        computer_choice = 'rock'
    elif randon_number == 1:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissors'

    user_choice = input("Please enter ROCK, PAPER or SCISSORS: ").lower()

    if user_choice == computer_choice:
        print('It is a DRAW')

    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print('computer win'.upper(), 'Paper covers the Rock')
            computer += 1 
        elif computer_choice == 'scissors':
            print('You win'.upper(), 'Rock breaks the scissors')
            you += 1

    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('You win'.upper(), 'Paper covers the Rock')
            you += 1
        elif computer_choice == 'scissors':
            print('computer win'.upper(), 'scissors cuts paper')
            computer += 1

    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('computer win'.upper(), 'Rock breaks the scissors')
            computer += 1
        elif computer_choice == 'paper':
            print('You win'.upper(), 'scissors cuts paper')
            you += 1

if computer > you:
    print(f'Computer WON {computer} out of 5 rounds')
elif computer == you:
    print('Play again! It was a DRAW')
else:
    print(f'You WON {you} out of 5 rounds')