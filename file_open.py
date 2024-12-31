with open('test.txt') as test_file:
    print(test_file.read())
    
with open('test.txt') as test_file:
    print(test_file.readlines())
# приводит текст файла в список

with open('new.txt', 'w') as new_file:
    new_file.write("First line in the new file\n")
    # запись в файле причем старый файл перезапишется 
with open('new.txt') as new_file:
    print(new_file.read())
    
with open('new.txt', 'a') as new_file:
    new_file.write("Second line in the new file\n")
    # открыть файл для дозаписи 'a' строка будет добавлена 
    
# удаление файла 

# from pathlib import Path
# print(Path('new.txt').exists()) поиск файла
# Path('new.txt').unlink() удаление файла
# print(Path('new.txt').exists()) повторный поиск