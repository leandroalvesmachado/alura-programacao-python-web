from codigo.bytebank import Funcionario

# pytest exige o método iniciar test_
# interessante o nome do método ser o mais verboso e explicativo possível
# Metodologia Givern-When-Then, Dado(contexto), Quando(ação), Então(desfecho)
# GIVEN — Contexto: entrada da data de nascimento
# WHEN — Ação: chamada do método idade
# THEN — Desfecho: verificação se resultado é igual ao esperado
# pytest -v para retorno mais detalhado do teste

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