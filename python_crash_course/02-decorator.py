def give_a_string(func):
    def wrapper():
        print('Please input a your Name')
        name = input()
        func()
        print(name)
    return wrapper

@give_a_string
def getName():
    print('\nHi ')
    
getName()


        