url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

# bytebank.com/cambio?moedaOrigem=real
print(url)

# string metodo find, retorna a posição do caractere
indice_interrogacao = url.find('?')

# fatiamento de strings

# url_base = url[0:indice_interrogacao]
url_base = url[:indice_interrogacao]
print(url_base) # Vai imprimir bytebank.com/cambio

url_parametros = url[indice_interrogacao+1:]
print(url_parametros) # Vai imprimir moedaOrigem=real

parametro_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametro_busca)
print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]
print(valor)
