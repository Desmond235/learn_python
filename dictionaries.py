capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# print(capitals['USA'])
# print(capitals.get('USA'))

# if capitals.get('Ghana'):
#     print("That capital exists")
# else:
#     print("That capital does not exist")

# capitals.update({"Germany" : "Berlin"})
# capitals.pop('China')
# capitals.popitem()
# keys = capitals.keys()
#
# for key in capitals.values():
#     print(key)

# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f'{key} : {value}')