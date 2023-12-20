#regex para emails
import re

pattern_email = re.compile("[\w]+@gmail\.com[\.]*[a-zA-Z]{0,5}")
email = input('insira seu email = ')

while True:
    res_email = re.fullmatch(pattern_email, email)
    if res_email:
        print('email ok!')
        break
    else:
        email = input('insira seu email = ')