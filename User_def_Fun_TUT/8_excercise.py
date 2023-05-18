cart = []

def showCart():
    '''Print items in cart'''
    if not cart == []:
        for items in cart:
            print(items)
    else:
        print('Cart is empty')

def addItem(item):
    '''Takes item and append it to cart'''
    cart.append(item)
    print(item,' is added')

def removeItem(item):
    '''Takes item and remove it from the cart'''
    if item in cart:
        cart.remove(item)
        print(item,' is removed')

def clearCart():
    '''Clears items from cart and print that cart is empty'''
    cart.clear()
    print('Cart is empty')

def main():
    done = False

    while not done:
        ans = input('quit/add/remove/show/clear: ').lower()
        if ans == 'quit':
            print('Thank you for using our program')
            showCart()
            done = True

        elif ans == 'add':
            item = input('What would you like to add?: ').title()
            addItem(item)

        elif ans == 'remove':
            showCart()
            item = input("What would you like to remove?: ").title()
            removeItem(item)

        elif ans == 'show':
            showCart()

        elif ans == 'clear':
            clearCart()

        else:
            print('Sorry that was not an option')

main();

