endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# o search() quando queremos buscar um padrão dentro de uma string inteira e o 
# match() quando queremos verificar se a nossa string inteira bate com aquele padrão.

import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos


# melhorado
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
padrao = re.compile("[0123456789]{5}[-]{0,1}[0123456789]{3}")

# search = verifica se existe o padrão na string que queremos
busca = padrao.search(endereco)  # Match

if busca:
    cep = busca.group()
    print(cep)