a = 10 

def my_fn():
    a = True
    b = 15
    print(a)
    print(b)

c = 5

def my_func():
    def inner_fn():
        print(c)
    inner_fn()

my_func()

def my_fuction():
    global g 
    g = 12 
my_fuction()
print(g)

k = 13

def my_functi():
    global k
    k = 15
my_functi()
print(k)

q = 5
def my_f(z,s):
    r = 10
    print(q)
    print(z, s)
    print(dir())
my_f(3, 5)


