maintance = True
list_toppings = ['mushroom', 'pineapple', 'bacon']
list_user_add = []

def pizzaTopping():
    global list_user_add;
    print('The toppings on your pizza are:')
    for items in list_user_add:
        print(' ',items, end=' ')
    print()

print('Welcome to Cavendish Pizzeria - choose your topping')
print('When prompted, enter first letter or full word of operation')
print('----Operations---- \na.  Add a topping \nr.  Remove a topping \no.  Order the pizza \nq.  Quit \ns   Start Over \nc.  Change Topping')

while maintance:
    options = input('What would you like to do? \n    add, remove, order, quit, startover, change: ')

    if options.lower() == 'add' or options.lower() =='a': 
        for items in list_toppings:
            print('*', items)

        topping = input('Select and Type a topping to add: ')
        if topping.lower() in list_toppings:
            list_user_add.append(topping.lower())
        else:
            print("I'm not sure what you said, please try again.")

        pizzaTopping();        
    
    elif options.lower() == 'remove' or options.lower() == 'r':

        remove_topping = input('What topping would you like to remove: ').lower()

        if remove_topping in (list_user_add):
            list_user_add.remove(remove_topping)
        
        else:
            ("You haven't added ",remove_topping,' as a topping')

        pizzaTopping();

    elif options.lower() == 'order' or options.lower() == 'o':
        pizzaTopping();
        print('Thanks for your order !')

        new_order = input('Do you want to place another order ?(yes/no): ')

        if new_order.lower() == 'yes' or new_order.lower() == 'y':
            list_user_add = []
            continue;
        elif new_order.lower() == 'no' or new_order.lower() == 'n':
            maintance = False
        else:
            print('Unrecognized response')
            continue;
    
    elif options.lower() == 'quit' or options.lower() == 'q':
        exit = input("Are you sure you want to quit (yes/no): ")       

        if exit.lower() == 'yes' or exit.lower() == 'y':
            break;
        elif exit.lower() == 'no' or exit.lower() == 'n':
            pass;
        else:
            print('Unrecognized response')
            continue;
    
    elif options.lower() == 'startover' or options.lower() == 's':
        print('You can Start again now')
        list_user_add = []
        continue;
        
    elif options.lower() == 'change' or options.lower() == 'c':
        change_topping = input('What topping do you want to change: ')
        if change_topping.lower() in list_user_add:
            replace_topping = input('What topping do you want to replace for it: ').lower()
            if replace_topping in list_toppings:
                list_user_add.remove(change_topping)
                list_user_add.append(replace_topping)
                pizzaTopping();
            else:
                print("There is no such a topping available")
        else:
            if change_topping in list_toppings:
                print("You haven't add this as a topping")
            else:
                print('no such topping is available')
    
    else:
        print('Invalid Option entered. Try Again')
