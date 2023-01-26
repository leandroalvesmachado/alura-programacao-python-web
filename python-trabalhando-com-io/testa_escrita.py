# w = Quando a gente abre o arquivo no modo “W”, ele "trunca" o arquivo primeiro. 
# Ou seja, se o arquivo existir, e já houver um arquivo com aquele nome, 
# ele vai apagar o conteúdo dele e realizar as inserções
# arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')

# a = modo de append. É um modo que vai colocar um novo dado, que no nosso caso é um novo contato, 
# ao final do arquivo, sem apagar o restante
# se o arquivo não existir, ele cria o arquivo
# arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a')

# arquivo no modo tanto de escrita, quanto o de leitura
arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w+')

contatos = [
    '11,Carol,carol@carol.com.br\n',
    '12,Ana,ana@ana.com.br\n',
    '13,Tais,tais@tais.com.br\n',
    '14,Felipe,felipe@felipe.com.br\n'
]

# escreve no arquivo
# arquivo_contatos.write(contatos)

# escreve várias linhas no arquivo
for contato in contatos:
    arquivo_contatos.write(contato)

# fechando o arquivo
# arquivo_contatos.flush()
arquivo_contatos.close()

arquivo_contatos.seek(28)
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha)