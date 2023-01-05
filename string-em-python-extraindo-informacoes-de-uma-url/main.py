# url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
url = " "

# Sanitização da URL
url = url.replace(" ", "")

# Validação da URL
if url == "":
    # quando quer retornar um erro
    raise ValueError("A URL está vazia")

# fatiamento de strings

# bytebank.com/cambio?moedaOrigem=real
print(url)

# string metodo find, retorna a posição do caractere
# Separa a base e os parametros
indice_interrogacao = url.find('?')

# url_base = url[0:indice_interrogacao]
url_base = url[:indice_interrogacao]
print(url_base) # Vai imprimir bytebank.com/cambio

url_parametros = url[indice_interrogacao+1:]
print(url_parametros) # Vai imprimir moedaOrigem=real


# Busca o valdor de um parâmetro
parametro_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametro_busca)
print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if (indice_e_comercial == -1):
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
