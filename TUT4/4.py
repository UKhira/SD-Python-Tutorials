sum = 0
for i in range(0,5):
    n = input('Enter a Number \n')
    try:
        n = int(n)
        sum+= n
    except ValueError:
        print('You must enter an integer')
        continue;
print('Total = ',sum)
