secret = 'water'
turns = 6
guesses =''

print('Guess the Idden Word \nYou have 6 turns left \n','_ '*6)
while turns > 0:
    guess = input("\nGuess a Letter ").lower()
    guesses += guess[0]
    for letter in secret:
        if letter in guesses:
            print(letter,'',end='')
        else:
            print('_',end=' ')
print("\nEnd of Game")
