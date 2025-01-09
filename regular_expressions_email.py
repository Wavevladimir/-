import re


def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "Valid" if email_check_pattern.fullmatch(email) else "Not valid"
    return (email, validation_result)
    
# Valid
print(check_email('bs@gmail.com'))
print(check_email('b_s@gmail.com'))
print(check_email('b.s@gmail.com'))
print(check_email('b.s@sub.gmail.com'))
# Invalid
print(check_email('@gmail.com'))
print(check_email('bsgmail.com'))
print(check_email('bs@'))