age = input('Enter Your age: \n')
try:
    age = int(age)
    if age >= 18:
        print('You can vote')
except ValueError:
    print('Age must be an integer')
