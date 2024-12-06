#False
#int 0
#float 0.0
#complex 0j

print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(None))

print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(range(0)))
print(bool(()))
print(bool(''))

print(not not {})

my_list = [1, 2]
if len(my_list) > 0:
    print("Last him elements")