def decoration_fuction(original_fn):
    def wrapper_fn(a, b):
        print("Executed before function")
        result = original_fn(a, b)
        print("Executed after function")

        return result
    return wrapper_fn

@decoration_fuction
def my_function(a, b):
    print("This is my function!")
    return (a , b)

result = my_function(100, 50)
print(result)