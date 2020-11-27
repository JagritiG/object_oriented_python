# Decorators
# Decorators allow programmers to modify the behavior of the function or class.
# Decorators allow to wrap another function in order to modify the behavior of wrapped function.


# Example-1: actual function without return value
# define a decorator
def decorator_func1(func):

    # define a wrapper function in which the argument is called
    def wrapper_func():
        print("This is a wrapper function")

        # Call the actual function
        func()

        print("Actual function execution done")

    return wrapper_func


# define the function to be called inside wrapper
def wrapped_func():
    print("This is the actual wrapped function")


# pass add() inside the decorator to control its behavior
wrapped_func = decorator_func1(wrapped_func)


# Example-2: actual function with returned value
# define a decorator
def decorator_func2(func):

    # define a wrapper function in which the argument is called
    def wrapper_func(*args, **kwargs):
        print("This is a wrapper function")

        # Call the actual function
        # getting the returned value
        result = func(*args, **kwargs)

        print("Actual function execution done")

        # return the result
        return result

    return wrapper_func


# adding decorator to the function
@decorator_func2
def add_nums(num1, num2, *args, **kwargs):
    print("This is the actual wrapped function")
    result = num1 + num2 + sum(arg for arg in args) + sum(arg for arg in kwargs)
    return result


if __name__ == "__main__":

    # calling the function
    wrapped_func()

    # calling add_nums() function
    a, b, c = 2, 4, 6
    print("Sum = ", add_nums(a, b, c, 7, 1))


