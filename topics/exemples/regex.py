#validador de cadastro
import re

pattern_cpf = re.compile("[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}")
pattern_email = re.compile("[\w]+@gmail\.com[\.]*[a-zA-Z]{0,5}")

email = input('insira seu email = ')
cpf = input('informe seu cpf = ')

res_email = re.fullmatch(pattern_email, email)
res_cpf = re.fullmatch(pattern_cpf, cpf)

while True:
    res_email = re.search(pattern_email, email)
    res_cpf = re.fullmatch(pattern_cpf, cpf)
    if res_cpf and res_email:
        print('cadastro ok!')
        break
    else:
        email = input('insira seu email = ')
        cpf = input('informe seu cpf = ')