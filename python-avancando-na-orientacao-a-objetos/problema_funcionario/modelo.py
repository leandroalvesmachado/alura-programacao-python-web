# Para a tomada de decisão sobre qual método deverá ser executado quando temos diversas superclasses que o possuem, internamente, 
# a versão 3 do Python usa um algoritmo chamado MRO (Method Resolution Order), 
# com um funcionamento que começa a busca pela classe atual, que é a própria classe.

# Além disto, o cálculo do algoritmo acessará não apenas esta classe, mas todas as classes mães de Alura, 
# e assim por diante, hierarquicamente:
# Pleno > Alura > Funcionario > Caelum > Funcionario

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print("Horas registradas...")
    
    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster():
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior()
jose.busca_perguntas_sem_resposta()
# jose.mostrar_tarefas()

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

# MRO (Method Resolution Order)
# Pleno > Alura > Funcionario > Caelum > Funcionario

joao = Senior('joao')
print(joao)