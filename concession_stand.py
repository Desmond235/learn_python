
# concession stand program

menu = {
    "banku" : 4.40,
    "beans" : 2.50,
    'yam': 1.00,
    'tacos': 2.35,
    'kenkey' : 3.90,
    'eba' : 4.58,
    'rice' : 2.00,
    'fries' : 5.00
}

cart =  []
total = 0

print('---------- MENU ----------')
for key, value in menu.items():
    print(f'{key:10}: {value:.2f}')
print('---------------------------')
print()

while True:
    food = input('Select food (q to quit): ').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print('--------- YOUR ORDERS ---------')  

for food in cart:
    total += menu.get(food)
    print(food, end= " ")

print()
print(f'Your total is: ${total}')    