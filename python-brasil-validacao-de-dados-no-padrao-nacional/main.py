from cpf_cnpj import Documento
import re # import para utilizar expressão regular
from telefonebr import TelefoneBr
from datetime import datetime, timedelta # import para trabalhar com datas
from databr import DataBr
from acesso_cep import BuscaEndereco
import requests # para requisições http

# 1 - Validando CPF e acessando o PYPI

cpf = "47252994058"
objeto_cpf = Documento.cria_documento(cpf)
print(objeto_cpf)

# 2 - Validando CNPJ e construindo uma Factory
print("\n")

exemplo_cnpj = "63354260000185"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)


# 3 - Validando telefones com expressões regulares
print("\n")

# []	Define um range ou um grupo de caracteres	            [0-9]; [a-z]; [abc]
# * 	Marca nenhuma, uma ou mais ocorrências	                sol*
# {}	Quantidade de repetições de uma ocorrência definida	    [abc]{5}
# \d	Qualquer número de 0 até 9	                            \d{3,4}
# \w	Qualquer número de a té 9 letra de a até z ou _	        \w{10}
# |	    Um ou outro	                                            @$
# ()	Captura e agrupa	                                    (\w{4})

# O método usado para podermos buscar é o search(), que buscará o padrao dentro de um texto como resposta
# padrao = "[0-9][a-z][0-9]"
# texto = "123 1a2 1cc aa1"
# resposta = re.search(padrao, texto)
# print(resposta)
# print(resposta.group())

# padrao_email = "\w{5,50}@[a-z]{3,10}.com.br"
# texto_email = "aaabbbcc rodrigo123@gmail.com.br"
# resposta_email = re.search(padrao_email, texto_email)
# print(resposta_email.group())

# validando lista telefônica com expressão regular
# ? = opcional conteudo a esquedar da interrogação
# padrao_molde = "(xx)aaaa-wwww"
# padrao_telefone = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
# texto_telefone = "eu gosto do numero 2126451234"
# resposta_telefone = re.search(padrao_telefone, texto_telefone)
# print(resposta_telefone)

telefone = "558530447295"
telefone_objeto = TelefoneBr(telefone)
print(telefone_objeto)

# 4 - Manipulando e formatando datas
print("\n")

# %A retorna os dias da semana por extenso, como Sunday;
# %d exibe os dias do mês com números de 01 a 31;
# %m retorna meses em números de 01 a 12;
# %y mostra o ano com apenas dois dígitos;
# %Y apresenta o ano em formato de quatro números;
# %H retorna o horário no formato decimal, como 00, 001 e etc;
# %M exibe os minutos de forma decimal;
# %S apresenta os segundos em decimal.

# print(datetime.today()) # 2023-01-18 12:58:07.965952

hoje = datetime.today()
hoje_formatada1 = hoje.strftime("%Y")
hoje_formatada2 = hoje.strftime("%d/%m/%Y")
hoje_formatada3 = hoje.strftime("%d/%m/%Y %H:%M")

print(hoje)
print(hoje_formatada1)
print(hoje_formatada2)
print(hoje_formatada3)
print(type(hoje_formatada1)) # hoje_formatada1
print("\n")

cadastro = DataBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro.tempo_cadastro())
print(cadastro)
print("\n")

# Na documentação do python fica na seção Emulating numeric types
# __add()__ corresponde à operação de soma +;
# __sub()__ faz a subtração -;
# __mul()__ faz a multiplicação *.

numero1 = 1
numero2 = 2
string = "um"

print(len(string))
print(numero1 + numero2)

hoje = datetime.today()
amanha = datetime.today()
print(hoje - amanha)

# timedelta
# de alguma forma de somar dias, horas ou meses à variável amanha
# usaremos o timedelta() que faz este tipo de soma em uma data, entre outras ações
# timedelta serve para operações com datas, algo parecido com o Carbon do laravel
hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1)
print(hoje - amanha)


# 5 - Trabalhando com CEP e acessando uma API
print("\n")

cep = "01001000"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

# r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
# print(r)
# print(r.text)

a = objeto_cep.acessa_via_cep()
print(a)
print(dir(a)) # lista os métodos que o elemento tem disponível
# print(type(a))
# print(a.text)
# print(a.json())
# print(a.json()['cep'])
# print(a.json()['bairro'])
# print(type(a.text))
# print(type(a.json()))

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

bairro, cidade, uf = objeto_cep.retorna_endereco()
print(bairro, cidade, uf)
