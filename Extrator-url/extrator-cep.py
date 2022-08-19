
endereco = "Rua das Rosas, 672; Apto 155. Urca - RJ/RJ. 23456789"

import re   # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos      # como funciona um cep...

# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
# padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")     # Ao invés do hífen, codificador {0,1} aparece ou não...
                # poderia ser, por exemplo, [a-z], para letras...


busca = padrao.search(endereco)     # Método Match (acha ou dá None)    # "?" Busca, tendo hifen ou não

if busca:
    cep = busca.group()
    print(cep)
