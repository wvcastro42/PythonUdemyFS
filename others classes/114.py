'''
Example for decorators

def hello(name="maria"):
    print("Hello() function has been run...")
    def greet():
        return "this is inside greet()"
    def welcome():
        return "this is inside welcome()"


    if name == "jose":
        return greet
    return welcome

x = hello()
print(x())
'''
# def hello():
#     return "Hi Weverton"
#
#
# def other(func):
#     print("Hello")
#     print(func())
#
# other(hello)

def new_decorator(func):

    def wrap_func():
        print("Code here before executing FUNC")
        func()
        print("Func() has been called!")

    return wrap_func

# func_needs_decorator = new_decorator(func_needs_decorator)  is the same as doing this: @new_decorator
@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator!")

func_needs_decorator()
