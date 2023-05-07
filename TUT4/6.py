stars = input('How many starts do you want to display \n')
try:
    stars = int(stars)
    for x in range(0,stars):
        print('*', end=' ')
    
except ValueError:
    print('Integer required')
