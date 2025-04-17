
# *args
# def display_name(*args):
#     for arg in args:
#         print(arg, end= " ")
#
# display_name('Desmond', "Adabe")

# **kwargs
# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key:8}: {value}")
#
# print_address(street="345 makeup street",
#                     city='Accra',
#                     region="Greater Accra",
#                     gps='GA-003-2090')

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if 'apt' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif 'pobox' in kwargs:
        print(f'{kwargs.get('street')}')
        print(f'{kwargs.get('pobox')}')
    else:
        print(f'{kwargs.get('street')}')

    print(f'{kwargs.get('city')} {kwargs.get('region')} {kwargs.get('zip')}')
shipping_label("Dr.", "Desmond", "Mawuta", "III",
               street="123 makeup street",
               apt="#100",
               city="Accra",
               region='Greater Accra',
               zip='4984')


