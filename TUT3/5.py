ask = input('Do You like Python? (yes/no): \n')
if ask.lower()=='yes' or ask.lower() == 'y' :
    print('You are right on course')
elif ask.lower() == 'no' or ask.lower() == 'n':
    print('You might change your mind')
else:
    print('I do not understand')
