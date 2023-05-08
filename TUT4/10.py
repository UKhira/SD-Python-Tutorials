import random

guess_validator = False
guessTaken = 0

print("Guess the Hidden Number \n Hint: It's between 1 and 20 \n You have Maximum five attempts")
hidden = random.randint(1,20)
print(hidden)

for attempt in range(5):
	guess = input("Enter your guess : ")
	try:
		guess = int(guess)
		guessTaken+=1
		if guess in range(0,20):
			if guess == hidden:
				guess_validator = True
				break;
			elif guess < hidden:
				print("Your guess is too low")
			else:
				print("Your guess is too high")			
		else:
			print("Guess is out of range. pick a number between 1 and 20")
    
	except Exception:
		print("Guess should be an integer")

if guess_validator == True:
	print("Guess is correct. \nYou got it in ",guessTaken," guesses")
else:
	print("Not Guessed. The correct answer was ",hidden)
