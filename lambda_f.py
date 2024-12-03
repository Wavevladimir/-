#def mult(a, b):
#    return a * b

mult = lambda a, b: a * b

print(mult(10, 5))

def greeting(greet): 
    def info(name):
        return f"{greet}, {name}!"
    return info
    #return lambda name: f"{greet}, {name}!"
morning_greeting = greeting("Good Morning")
print(morning_greeting('Vova'))

evening_greeting = greeting("Good Evening")
print(evening_greeting('Vova'))