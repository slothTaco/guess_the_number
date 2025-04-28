# This is a guess the number game.
import random

guessTaken = 0

print('Hello! What is yout name?')
myName = input()

number = random.randint(1,20)
print('Well, '+ myName + ', I am thinking of a number between 1 and 20. '
     + 'Can you guest it in six turns?')

for guessTaken in range(6):
    print('take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is to low')

    if guess > number:
        print('Your guess is to high.')

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' +
          guessTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
