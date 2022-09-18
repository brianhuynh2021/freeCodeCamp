
# Reference from Stackoverflow
def my_decorator(some_function):
    def my_wrapper():
        print("do something before")   #do something before, if you want to
        some_function()
        print("do something after" )  #do something after, if you want to
    return my_wrapper

@my_decorator
def orig_func():
   print("Wheee!")


orig_func()

# birthday cake 