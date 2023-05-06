n1 = int(input('Enter a Number: '))
operator = input('Pick an Operator \n+ \n- \n* \n\ \nEnter Operator: ')
n2 = int(input('Enter another Number: '))
if operator == '+' :
    answer = n1 + n2
elif operator == '-' :
    answer = n1 - n2
elif operator == '*' :
    answer = n1 * n2
elif operator == '/':
    try:
        answer = n1 / n2
    except Exception as e:
        print(e)
else :
    answer = 'Invalid Operator Entered Try Again'
