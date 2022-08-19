
    # URL válidas:
# bytebank.com/cambio
# bytebank.com.br/cambio
# www.bytebank.com/cambio
# www.bytebank.com.br/cambio
# http://www.bytebank.com/cambio
# http://www.bytebank.com.br/cambio
# https://www.bytebank.com/cambio
# https://www.bytebank.com.br/cambio

    # URL inválidas:
# https://bytebank/cambio
# https://bytebank.naoexiste/cambio
# ht://bytebank.naoexiste/cambio

import re

# url = "https://www.bytebank.com.br/cambio"    # padrão de url escolhido
# url = "htps://www.bytebank.com.br/cambio"    # teste com erro "htps..."
url = "www.bytebank.com.br/cambio"    # teste com acerto, sem o "http://"...

padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida")
else:
    print("A URL é válida")
