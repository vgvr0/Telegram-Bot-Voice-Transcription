import bcrypt
import secrets



secret = secrets.token_hex(32)

hashed_login = bcrypt.hashpw(b"your_login", bcrypt.gensalt())
hashed_password = bcrypt.hashpw(b"your_password", bcrypt.gensalt())


print('Secret: ', secret)

print('\nlogin: ', hashed_login)

print('\npassword: ', hashed_password)