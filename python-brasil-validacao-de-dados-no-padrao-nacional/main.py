# from validate_docbr import CPF
# from cpf_cnpj import CpfCnpj

from cpf_cnpj import Documento
import re # import para utilizar expressão regular
from telefonebr import TelefoneBr

# []	Define um range ou um grupo de caracteres	            [0-9]; [a-z]; [abc]
# * 	Marca nenhuma, uma ou mais ocorrências	                sol*
# {}	Quantidade de repetições de uma ocorrência definida	    [abc]{5}
# \d	Qualquer número de 0 até 9	                            \d{3,4}
# \w	Qualquer número de a té 9 letra de a até z ou _	        \w{10}
# |	    Um ou outro	                                            @$
# ()	Captura e agrupa	                                    (\w{4})

# cpf = "47252994058"
# objeto_cpf = CpfCnpj(cpf, "cpf")

# print(objeto_cpf)

# cnpj = "63354260000185"
# objeto_cnpj = CpfCnpj(cnpj, "cnpj")

# print(objeto_cnpj)

exemplo_cnpj = "63354260000185"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

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


