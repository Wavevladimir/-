import re

test_password = '123AS!'

def check_password(password):
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"[a-z]+")
    uppercase_pattern = re.compile(r"[A-Z]+")
    number_pattern = re.compile(r"[0-9]+")
    special_symbol_pattern = re.compile(r"[@%#!&*^]+")
    
    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at list 8 symbols")
    
    print(check_password(test_password))