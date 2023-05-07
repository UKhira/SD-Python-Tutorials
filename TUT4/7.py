import random
count = 0

for a in range(0,100):
    dice_1 = random.randint(1,6)
    #print('Dice 1 = ',dice_1)      #to make sure code works properly
    dice_2 = random.randint(1,6)
    #print('Dice 2 = ',dice_2)      #to make sure code works properly
    if dice_1 == dice_2:
        count+=1
print('Out of 100 you rolled ',count,' doubles')
        
    

