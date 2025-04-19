from script1 import *

def favorite_drink(drink):
    print(f'Your favorite drink is {drink}')

def main():
    print("This is script2")
    favorite_food("hotdog")
    favorite_drink('coke')
    print('Goodbye!')

if __name__ == '__main__':
    main()