
class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flasp!')


class Person:

    def quack(self):
        print('I am Quacking like a duck')

    def fly(self):
        print('I am flapping my Arms')

def quack_and_fly(thing):

    # if isinstance(thing,Person):
    # thing.quack()
    # thing.fly()
    # else:
    #     print('This has to be a duck')
    #anohter method
    # if hasattr(thing, 'quacks'):
    #     if callable(thing.quack()):
    #         thing.quack()

    # if hasattr(thing,'fly'):
    #     if callable(thing.fly()):
    #         thing.fly

    #another method
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)

    print()



d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

