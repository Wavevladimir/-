import re

email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"

email_check_pattern = re.compile(email_regexp)
print(email_check_pattern.fullmatch('bs@gmail.com'))