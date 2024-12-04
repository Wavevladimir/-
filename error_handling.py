try:
    print(10 / 2)
except ZeroDivisionError as e: 
    print(type(e))
    print(e)
except TypeError as e:
    print(e)
else:
    print("There was no error")
finally:
    print('Continue...')

try:
    print(5 / 0)
except Exception as a: #любые типы ошибок можно описать этим
    print(a)

try:
    print(6 / 0)
except: #Либо так
    print("Some error occurred")

def divide_nums(a, b):
    if b == 0:
        raise TypeError("Second argument can't be 0")
    return a / b

try: 
    divide_nums(10, 0)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
print("Continue..")
