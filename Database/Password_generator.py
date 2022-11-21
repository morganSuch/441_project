import secrets
import string

#defining alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

total_chars = letters + digits + special_chars

def create_password:
      #password length
      user_passLength = input("How long do you want your password being? Minimum recommended is 10. ")

      #creating password that has certain constraints
      while True:
          password = ""
          for i in range(user_passLength):
                password += "".join(secrets.choice(total_chars))

          if (any(char in special_chars for char in password) and
              sum(char in digits for char in password)>=2):
                break
