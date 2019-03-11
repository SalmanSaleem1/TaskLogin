from datetime import datetime
# first = 'Salman'
# last = 'saleem'
#
# # sentence = 'My name is {} {}'.format(first, last)
# #
# # print(sentence)
#
# sentence = f'My name is {first.upper()} {last.islower()}'
# print(sentence)

# person = {'name':'Salman','age':23}
#
# # sentence = 'My name is {} and my age is {}'.format(person['name'],person['age'])
# # print(sentence)
#
# sentence = f"My name is {person['name']} and my age is {person['age']}"
# print(sentence)

# calculation = f'4 times 11 = {4*11}'
# print(calculation)

# for n in range(1,11):
#     sentence = f'Range = {n:04}'
#     print(sentence)

# pi = 3.140145556
#
# sentence = f'The value of pi {pi:.2f}'
# print(sentence)

birthday = datetime(1990, 1, 2)
sentence = f'My birthday date is {birthday:%B,%m,%Y}'
print(sentence)

