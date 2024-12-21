import module_practic_one as mod_one, my_fn
# from module_practic_one import my_name, print_sum as sum
# sum(5, 2)
# print(my_name)

print(mod_one)
print(type(mod_one))
print(dir(mod_one))

print(mod_one.my_name)
mod_one.print_sum(5, 3)

print(__name__)
print(__name__ == '__main__')

