value = int(input('Enter Number 1 to convert Celsius to Fahrenheit.  \nEnter Number 2 to convert Fahrenheit to Celsius. \n'))
if value == 1:
    temp = float(input('Enter Temperature: '))
    a = (temp * 1.8) + 32
elif value == 2:
    temp = float(input('Enter Temperature: '))
    a = (temp - 32)/1.8
else:
    a = 'Invalid Option Entered'
print(a)
