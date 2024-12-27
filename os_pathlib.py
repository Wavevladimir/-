from os import path
print(path.abspath('.'))
print(type(path))

from pathlib import Path
print(Path('.').absolute())
print(type(Path))

file_path = Path('test.txt')
print([m for m in dir(file_path)
       if not m.startswith('_')])
# все методы которые можно использовать с файлами без магических

from pathlib import Path
print(Path.cwd())
# путь к файлу выбранному

print(Path('usr').joinpath('local').joinpath('bin'))
print(Path('usr') / 'local' / 'bin')
# создание новых путей 

print(Path('main.py').exists())

print(Path('main.py').is_file())
# директория или файл
print(Path('../python').is_dir())

# список файлов и папок 
from pathlib import Path

for f in Path('.').iterdir():
    print(f)