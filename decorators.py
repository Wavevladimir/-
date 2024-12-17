def decoration_fuction(original_fn):
    def wrapper_fn():
        print("Executed before function")
        result = original_fn()

        return result
    return wrapper_fn

@decoration_fuction
def my_function():
    print("This is my function!")

my_function()