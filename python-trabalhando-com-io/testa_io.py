arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')

# <class '_io.TextIOWrapper'>
print(type(arquivo))

# <class '_io.BufferedReader'>
print(type(arquivo.buffer))

conteudo = arquivo.buffer.read()

# b'1,Guilherme,guilherme@guilherme.com.br\n2,Elias,elias@elias.com.br\n, .....'
# print(conteudo)

# b = informa que o valor é em bytes
texto_em_bytes1 = b'Esse e um texto em bytes'
print(texto_em_bytes1)
# <class 'bytes'>
print(type(texto_em_bytes1))

# assim é possível usar bytes com acentos
texto_em_bytes2 = bytes('Esse é um texto em bytes', 'latin_1')
print(texto_em_bytes2)
# <class 'bytes'>
print(type(texto_em_bytes2))

# escrevendo em bytes
contato = bytes('15,Verônica,veronica@veronica.com.br', 'latin_1')
arquivo.buffer.write(contato)

arquivo.close()