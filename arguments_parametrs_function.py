#def my_fn(a,b): параметры
#    a = a + 1
#    c = a + b 
#    return c 
#my_fn(10, 3) аргументы

#def sum_nums(a, b):
#    c = a + b 
#    return(c)
#print(sum_nums(2, 5))

def sum_nums(*args):
    print(args)
    print(type(args))
    print(args[0])
    return sum(args)
print(sum_nums(2, 3, 7))

def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info
info = get_posts_info('Vova', 25)
print(info)