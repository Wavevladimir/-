import re

def check_password(password):
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")
    no_witespace_pattern = re.compile(r"^\S*$")
    
    if not re.fullmatch(no_witespace_pattern, password):
        return (False, "No witespaces allowed in the password")
    
    
    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at list 8 symbols")
    
    if not re.fullmatch(lowercase_pattern, password):
        return(False, "Password must have at least one lowercase letter")
    
    if not re.fullmatch(uppercase_pattern, password):
        return(False, "Password must have at least one uppercase letter")
    
    if not re.fullmatch(number_pattern, password):
        return(False, "Password must have at least one number")
    
    if not re.fullmatch(special_symbol_pattern, password):
        return(False, "Password must have at least one special symbol @%#!&*^")
    return (True, "Password is valid!")
    
# print(check_password('123asdDFG   %$'))
# print(check_password('123'))
# print(check_password('12345678'))
# print(check_password('1234567a'))
# print(check_password('asdbaDGAG'))
# print(check_password('3242sfASDF'))
# print(check_password('123asdDFG%$'))

while True:
    password = input("Please enter password: ")
    password_check_res = check_password(password)
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])