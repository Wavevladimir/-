def decoration_fuction(original_fn):
    def wrapper_fn(*args, **kwargs):
        print("Executed before function")
        result = original_fn(*args, **kwargs)
        print("Executed after function")

        return result
    return wrapper_fn

@decoration_fuction
def my_function(a, b):
    print("This is my function!")
    return (a , b)

result = my_function(100, 50)
print(result)