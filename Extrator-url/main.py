
url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
# url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
print(url)


# Sanitização da URL
# url = url.replace(" ", "")    # ou
# url = url.strip()
# print(url)

# Validação da URL
# if url == "":
#    raise ValueError("A URL está vazia.")


    # Separa base e os parâmetros.

indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)


    # Escolhe o parâmetro, e busca seu valor.

parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
# print(indice_parametro)

tamanho_parametro = len(parametro_busca)
indice_valor = indice_parametro + tamanho_parametro +1
# print(indice_valor)

indice_e_comercial = url_parametros.find("&", indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

# print(valor)
