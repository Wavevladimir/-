def log_function_call(fn):
    def wrapper(*args, **kwargs):
       print(f"Function name: {fn.__name__}")
       print(f"Function arguments: {args}, {kwargs}")
       result = fn(*args, **kwargs)
       print(f"Function result: {result}")
       return result
    return wrapper

@log_function_call
def mult(a, b):
    return a * b 

print(mult(2, 5))


@log_function_call
def sum(a, b):
    return a + b

print(sum(40, 20))