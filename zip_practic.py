from zipfile import ZipFile
from pathlib import Path

with ZipFile('my-files.zip', mode='r') as my_zip_file:
    my_zip_file.extractall('my-files-unzipped')
    print(my_zip_file.infolist())
    print(my_zip_file.filename)

# Path('my-files').mkdir()

# with open('my-files/first.txt', 'w') as my_file:
#     my_file.write("This is first file")
    
# with open('my-files/second.txt', 'w') as my_file:
#     my_file.write("This is second file") создание файлов которые мы запакуем

# with ZipFile('my-files.zip', mode='w') as my_zip_file:
#     # print(my_zip_file)
#     for file in Path('my-files').iterdir():
#         print(file)
#         my_zip_file.write(file) создания зип файла 