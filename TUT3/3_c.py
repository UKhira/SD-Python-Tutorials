cost = input('Enter the cost of meal: ')
rate = input('Pick a Rating for satisfactory level - \n1 = Totaly satisfied \n2 = Satisfied \n3 = Dissatisfied \nEnter Your Rate: ')
try:
    cost = float(cost)
    if rate == '1':
        tip = cost * (20/100)
    elif rate == '2':
        tip = cost * (15/100)
    elif rate == '3':
        tip = cost * (10/100)
    else :
        tip = 'Invalid Rate entered'
    print('Your satisfaction Level = ',int(rate), '\nTip =',round(tip,2))
except ValueError:
    print('Please Enter a valid cost')
