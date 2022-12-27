class Conta:
    
    # construtor
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto")
        # colocando o atributo como privado = __ (private)
        # _Conta__numero (possível acessar assim, mas não é o ideal)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
    
    # getters e setters
    # def get_numero(self):
    #     return self.__numero
    
    # def get_titular(self):
    #     return self.__titular

    # def get_saldo(self):
    #     return self.__saldo

    # def get_limite(self):
    #     return self.__limite

    # def set_limite(self, limite):
    #     self.__limite = limite

    # utilizando property nos atributos da conta
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # método estático que poode ser utilizado sem uma instância da classe (objeto)
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


    # métodos
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))
    
    def deposita(self, valor): 
        self.__saldo += valor

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
    
    # método privado (__), criado apenas para ser utilizado pelos métodos da propria classe
    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.__saldo + self.__limite)
    
    def transfere(self, valor, destino):
        # sel = conta de origem (objeto que esta executando o método)
        self.saca(valor)
        destino.deposita(valor)
