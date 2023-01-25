from codigo.bytebank import Funcionario
import pytest
from pytest import mark

# pytest exige o método iniciar test_
# interessante o nome do método ser o mais verboso e explicativo possível
# Metodologia Givern-When-Then, Dado(contexto), Quando(ação), Então(desfecho)
# GIVEN — Contexto: entrada da data de nascimento
# WHEN — Ação: chamada do método idade
# THEN — Desfecho: verificação se resultado é igual ao esperado
# pytest -v para retorno mais detalhado do teste
# python -k idade ou python -v -k idade executa o teste que possui no nome o texto idade (filtro), 
# tipo como se quisesse rodar um teste em específico
# @ = decorator
# pytest -v -m calcular_bonus, comando para executar testes com @mark
# Documentação pytest - https://docs.pytest.org/en/stable/index.html
# pip install pytest-cov, para cobertura de testes (coverage)
# pip freeze > requeriments.txt
# pytest --cov, pytest-cov procurará todos os testes para checar a cobertura
# pytest --cov=codigo tests/ , teste de cobertura informando o diretorio (codigo) e qual a pasta dos testes (tests/)
# pytest --cov=codigo tests/ --cov-report term-missing, funcionalidade igual a de cima, mas com relatório e informando local do problema (missing)
# pytest --cov=codigo tests/ --cov-report html = resultado do teste em html
# pytest --junitxml report.xml
# pytest --cov-report xml

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        #Given(Contexto)
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        # When(ação)
        resultado = funcionario_teste.idade()

        # Then(desfecho)
        assert resultado == esperado

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado # Then(desfecho)
    
    @mark.skip # pula o teste, ignora o teste
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus() # when

        assert resultado == esperado  # then

    # contruindo um teste que leva em consideração o exception
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            # teste em que o resultado esperado é uma exceção
            assert resultado  # then

    # def test_retorno_str(self):
    #     nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000 # given
    #     esperado = 'Funcionario(Teste, 12/03/2000, 1000)'
        
    #     funcionario_teste = Funcionario(nome, data_nascimento, salario)
    #     resultado = funcionario_teste.__str__() # when

    #     assert resultado == esperado #then