import random

input("Let's toss a coin \nPress Enter to toss a coin ")
toss = random.randint(0,1)
if toss == 0:
    print('Head')
else:
    print('Tails')

input("\nLet's roll a dice \nPress Enter to roll a dice ")
print(random.randint(1,6))
