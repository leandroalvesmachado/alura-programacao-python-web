try:
    # abrindo o arquivo informando o enconding
    # arquivo_contatos = open('dados/contatoss.csv', encoding='latin_1')

    # lê todas as linhas do arquivo
    # readlines() = ele devolve para a gente uma lista, onde cada item da lista, cada posição ali, é uma linha do arquivo CSV
    # conteudo = arquivo_contatos.readlines()

    # outra forma de ler o arquivo
    # retorna a primeira linha do arquivo
    # se chamar novamente o readline(), ele vai exibir a próxima linha, devido ao ponteiro
    # conteudo = arquivo_contatos.readline()

    # outra forma de ler o arquivo
    # readline(10) = retorna a primeira linha do arquivo com apenas 10 caracteres
    # conteudo = arquivo_contatos.readline(10)

    # abrindo o arquivo agora com o with (contexto)
    with open('dados/contatoss.csv', encoding='latin_1') as arquivo_contatos:
        for linha in arquivo_contatos:
            # por padrão o print utiliza o '\n' ao imprimir
            print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
finally:
    arquivo_contatos.close()
