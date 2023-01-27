import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            # id, nome, email = linha[0], linha[1], linha[2]
            # ja faz automaticamente na ordem das posições
            id, nome, email = linha
            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos


def contatos_para_pickle(contatos, caminho):
    # mode='wb' abre um arquivo em binário (bytes)
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)


def pickle_para_contatos(caminho):
    # mode='rb' lê um arquivo em binário (bytes)
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)
    
    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)



def _contato_para_json(contato):
    return contato.__dict__


def json_para_contatos(caminho):
    contatos = []

    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            # c = Contato(id=contato['id'], nome=contato['nome'], email=contato['email'])
            c = Contato(**contato) # ** = desempacotar os valores com o nome de mesmo parâmetro, como exibido no comentário anterior
            contatos.append(c)
    
    return contatos
