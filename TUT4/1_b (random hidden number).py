import random
hidden = random.randint(1,20)
#print(hidden)              #Use this line to make sure code works
guess = input('Guess the hidden number \n Hint: Number is between 1 and 20  \nEnter Your guess\n')
try:
    guess = int(guess)
    while guess != hidden:
        print('Guess is not Correct')
        guess = input('Guess Again: \n')
        try:
            guess = int(guess)
        except ValueError:
            print('Guess must be an integer between 1 and 20')
    print('Guess is correct')
except ValueError:
    print('Guess can only be a integer number')
