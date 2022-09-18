def get_some_texts(func):
    def wrapper(x, y):
        print("Please input x and y")
        return func(x,y)
    return wrapper

@get_some_texts
def add(x, y):
    return x+y


sum = add(5,6)
print('Total is: ', sum)