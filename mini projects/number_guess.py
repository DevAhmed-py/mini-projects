import random

while True:

    upper_band = input('Please enter the upper band of the guessing game: ')

    if upper_band.isdigit():
        upper_band = int(upper_band)
        if upper_band <= 0:
            print('Please enter a number greater than 0')
            continue
        else:
            break
    else:
        print('Please enter a Number')
        continue

random_numb = random.randint(0, upper_band)
guess = 0

while True:

    guess += 1
    user_guess = int(input('Please enter your guess: '))
    if user_guess == random_numb:
        print('You are Correct! :)')
        break

    elif user_guess > random_numb:
        print('Your guess is greater than the number. Try again!')
        continue

    else:
        print('Your guess is less than the number. Try again!')
        continue

print(f'You got the number after {guess} guesses :)')