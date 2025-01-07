import secrets
import string 

all_chars = string.ascii_letters + string.digits + string.punctuation

print(''.join(secrets.choice(all_chars) for i in range(8)))
# print(string.ascii_letters)
# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)

# print(string.ascii_letters + string.digits + string.punctuation)