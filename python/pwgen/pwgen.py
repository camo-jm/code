# this is basically an attempt at homemade encryption lollllllll
import secrets

keyword = str(input("enter your keyword: "))
password = secrets.token_hex( len(keyword) ) #huzzah
print(password)
