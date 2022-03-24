import random


guessesTaken=0

print('Hello! What is Your Name?  :')
MyName = input(": ")


number = random.randint(1,20)
print('Well, '  + MyName,  'I am Thinking of Number between 1 and 20: ')

for guessesTaken in range(6):
    print('Take a Guess. ')
    guess = input(': ')
    guess =int(guess)

    if guess < number:
        print('Your guess is Too low ')
    if guess > number:
        print('Your guess is Too high ')

    if guess == number:
        break
if guess == number:
    guessesTaken =str(guessesTaken + 1)
    print('Good Job, ' +  MyName  +  '! You Guess My number in '  +  guessesTaken +  '  guesses! ')



if guess != number:
    number = str(number)
    print('Nope. The Number I was thinking of was ' +  number +  '.')