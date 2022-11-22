

def verify_same(pass1, pass2):
  notMatch = True
  while notMatch:
    if pass1 == pass2:
      notMatch = False
    else:
      print("Your inputs did not match. Please try again.\n")
