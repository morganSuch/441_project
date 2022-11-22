import secrets
import string

#defining alphabet


def create_password(len):
      letters = string.ascii_letters
      digits = string.digits
      special_chars = string.punctuation
      total_chars = letters + digits + special_chars

      while True:
          password = ""
          for i in range(len):
                password += "".join(secrets.choice(total_chars))
          if (any(char in special_chars for char in password) and
              sum(char in digits for char in password)>=2):
                break
      print(password)
      return password

#create_password()