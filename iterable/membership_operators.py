#
# grades = {
#     "Desmond": "A",
#     "Frank": "B",
#     "Kounde": "C",
#     "Kylian": "D"
# }
#
# student = input('Enter the name of a student: ')
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f'{student} was not found')

email = 'desmond@gmail.com'

if '@' in email and "." in email:
    print('valid email')
else:
    print('invalid email')