print('WELCOME TO MY QUIZ GAME')

score = 0
playing = input('Do you want to play? ').lower()

if playing != 'yes':
    quit()

answer = input('Are you smart? ').lower()
if answer != 'yes':
    print("Apologies, You can't go further in the game")
    quit()
else:
    print("let's do this! :) ")

answer = input('How many continents on earth? ')
if answer == '7' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

answer = input('What company was initially known as "Blue Ribbon Sports"? ').lower()
if answer == 'nike' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

answer = input('What art form is described as "decorative handwriting or handwritten lettering"? ').lower()
if answer == 'calligraphy' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

answer = input('Which planet has the most moons? ').lower()
if answer == 'saturn' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

answer = input('What country has won the most World Cups? ').lower()
if answer == 'brazil' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

answer = input('Kratos is the main character of what video game series? ').lower()
if answer == 'god of war' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

answer = input('In what country would you find Mount Kilimanjaro? ').lower()
if answer == 'tanzania' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

answer = input('What is a group of pandas known as? ').lower()
if answer == 'an embarrassment' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

answer = input('What European country experienced the highest rate of population decline from 2015 - 2020? ').lower()
if answer == 'lithuania' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

answer = input('How many bones do we have in an ear? ')
if answer == '3' :
    print("Correct! :) ")
    score += 1
else:
    print("Wrong! :( ")

print(f'Your total score is {score}')
print(f'You got {int((score/10) * 100)}%')