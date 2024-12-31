test_file = open('test.txt', 'w')

print(test_file)
print(type(test_file))

test_file.write("First string\n")
test_file.write("Second string\n")

test_file.close()
test_file = open('test.txt')

print(test_file.read())

with open('test.txt', 'w') as test_file:
    test_file.write("First string\n")
    test_file.write("Second string\n")
    
with open('test.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break
