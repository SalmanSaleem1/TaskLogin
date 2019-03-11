

# person = {'name': 'Salman', 'age': 25, 'job': 'Programmer'}
# person = {'name': 'Salman', 'age': 25}

# if 'name' in person and 'age' in person and 'job' in person:
#     print("My name is {name} i am {age} year old and my job is {job}".format(**person))
# else:
#     print('Missing some element')

# try:
#     print("My name is {name} i am {age} year old and my job is {job}".format(**person))
# except KeyError as k:
#     print(f"Missin Key is {k}")

my_list = [1, 2, 3, 4, 5]

# if len(my_list)>=6:
#     print(my_list[5])
# else:
#     print('Index not found')

try:
    print(my_list[7])
except IndexError as I:
    print(I)