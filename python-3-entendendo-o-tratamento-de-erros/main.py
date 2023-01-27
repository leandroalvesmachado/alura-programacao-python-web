from pprint import pprint

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


cliente = Cliente('Jhon Doe', '123.456.789-00', 'Desenvolvedor')

# {'nome': 'Jhon Doe', 'cpf': '123.456.789-00', 'profissao': 'Desenvolvedor'}
print(cliente.__dict__)

# {'cpf': '123.456.789-00', 'nome': 'Jhon Doe', 'profissao': 'Desenvolvedor'}
pprint(cliente.__dict__, width=40)