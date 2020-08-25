#at least 8 characters long
#can contain any sort letter, numbers, symobols
import re

def password_checker():
  password = input('Please type your password:')

  if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print('Password is valid')
  else:
    print('Password is invalid')

password_checker()


def password_checker1():
  password1 = input('Please type your password:')
  pass_check = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')

  if pass_check.fullmatch(password1):
    print('Password is valid')
  else:
    print('Password is invalid')

password_checker1()