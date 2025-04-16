
price1 = 30000.14159
price2 = -9087.65
price3= 1200.34
name = 'Standard'

# if not isinstance(name, float):
#     print(f'{name} is not a number');

# print(f'Price 1 is ${price1:010}')
# print(f'Price 2 is ${price2:010}')
# print(f'Price 3 is ${price3:010}')

# justify
# print(f'Price 1 is ${price1:<10}')
# print(f'Price 2 is ${price2:<10}')
# print(f'Price 3 is ${price3:<10}')

# justify
# print(f'Price 1 is ${price1:>010}')
# print(f'Price 2 is ${price2:>010}')
# print(f'Price 3 is ${price3:>010}')

# Center
# print(f'Price 1 is ${price1:^10}')
# print(f'Price 2 is ${price2:^10}')
# print(f'Price 3 is ${price3:^10}')

# thousand operator
print(f'Price 1 is ${price1:+,.2f}')
print(f'Price 2 is ${price2:+,.2f}')
print(f'Price 3 is ${price3:+,.2f}')