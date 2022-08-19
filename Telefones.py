import re


padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
telefone = "552174316978"

resposta = re.search(padrao, telefone)
print("+{}({}){}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4)))
