import re
my_string = "My name is Vova."
res = re.search('V..a', my_string)
print(res)
print(type(res))
print(res.start())
print(res.end())
print(r"V..a\n.$")

my_pattern = re.compile(r'^My.*\.$')
print(my_pattern)
print(my_pattern.match(my_string))