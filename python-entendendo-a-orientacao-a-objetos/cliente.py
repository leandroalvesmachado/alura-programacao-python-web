class Cliente:

    # construtor
    def __init__(self, nome):
        self.__nome = nome
    
    # informa que o método trata uma propriedade da classe
    # só funciona quando o atributo esta private (__nome)
    # getter e setter com property
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome