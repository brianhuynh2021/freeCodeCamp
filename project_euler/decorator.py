#Decorator

def give_some_text(func):
    def wrapper():
        print('Before the main function')
        func()
        print('After the main fuction')
    return wrapper

# John this function 
@give_some_text
def hello_world():
    print('Hello world!')

hello_world()