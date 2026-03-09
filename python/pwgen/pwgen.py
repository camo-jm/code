# this is basically an attempt at homemade encryption lollllllll
import os
import secrets

keyword = str(input("enter your keyword"))

true_keyword = ""
for n in keyword:
    true_keyword += str(ord(n))

os.urandom()
