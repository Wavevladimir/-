from os import path 

# print(path.curdir) показывает относительный путь точкой
print(path.abspath('.'))

from pathlib import Path

print(type(Path))
# cwd = Path('.') найти отностиельный путь
cwd = Path('/Users').joinpath('wavevladimir').joinpath('git').joinpath('-')
print(isinstance(cwd, Path))
print(type(cwd))

print(Path.__subclasses__())
print(cwd.absolute())

print(cwd)

my_dir = Path('/Users') / 'wavevladimir' / 'git' / '-' / 'django'
# if not my_dir.exists(): если папки джанго не находит
    # my_dir.mkdir() то нужно создать эту папку
    
if my_dir.exists():
    my_dir.rmdir()