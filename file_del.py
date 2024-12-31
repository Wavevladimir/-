from pathlib import Path
file = open('test.txt', 'w')
file.close()

my_file = Path('test.txt')
if my_file.exists():
    my_file.unlink()