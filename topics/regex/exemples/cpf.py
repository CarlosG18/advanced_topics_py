#regex para cpf
import re

pattern_cpf = re.compile("[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}")
cpf = input('informe seu cpf = ')

while True:
    res_cpf = re.fullmatch(pattern_cpf, cpf)
    if res_cpf:
        print('cpf ok!')
        break
    else:
        print('cpf invalido! insira novamente no formato "xxx.xxx.xxx-xx"')
        cpf = input('informe seu cpf = ')