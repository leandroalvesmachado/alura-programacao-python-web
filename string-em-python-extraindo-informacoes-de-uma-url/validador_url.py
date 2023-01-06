# Exemplos de URLs válidas:
# bytebank.com/cambio
# bytebank.com.br/cambio
# www.bytebank.com/cambio
# www.bytebank.com.br/cambio
# http://www.bytebank.com/cambio
# http://www.bytebank.com.br/cambio
# https://www.bytebank.com/cambio
# https://www.bytebank.com.br/cambio

# Exemplos de URLs inválidas:
# https://bytebank/cambio
# https://bytebank.naoexiste/cambio
# ht://bytebank.naoexiste/cambio

# o search() quando queremos buscar um padrão dentro de uma string inteira e o 
# match() quando queremos verificar se a nossa string inteira bate com aquele padrão.

# Verifica se a base da URL está de acordo com o padrão correto

import re

# http(s)? pode ser http ou https
# bytebank.com(.br)? pode ter .com ou .com.br

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url) # match = verifica se é exatamente no padrão que queremos

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")