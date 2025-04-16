# temp = 25
# is_rainning = False

# if temp > 35 or temp < 0 or is_rainning:
#     print("The outdoor event is canceled")
# else:
#     print("The outdoor event is still scheduled")

temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT  outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print('it is could outside 🥶')
    print('It is sunny ☀️')
elif 28 > temp > 0 and is_sunny:
    print('It is warm outside 😑')
    print('It is sunny ☀️')
