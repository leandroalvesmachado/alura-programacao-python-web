class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self._likes} Likes')

    # representação textual do objeto
    def __str__(self) -> str:
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

# Herança da classe Programa
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # super chama o __init__ da classe mãe (programa)
        self.duracao = duracao

    # sobrescrita do método imprime da classe mãe (super)
    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self.duracao} - {self._likes} Likes')

    # representação textual do objeto
    def __str__(self) -> str:
        return f'{self._nome} - {self.ano} - {self.duracao} - {self._likes} Likes'


# Herança da classe Programa
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    # sobrescrita do método imprime da classe mãe (super)
    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self.temporadas} - {self._likes} Likes')

    # representação textual do objeto
    def __str__(self) -> str:
        return f'{self._nome} - {self.ano} - {self.temporadas} - {self._likes} Likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Python Data Model __metodo__ (existem mais)
    # Para quê?	            Método
    # Inicialização	        __init__
    # Representação	        __str__, __repr__
    # Container, sequência	__contains__, __iter__, __len__, __getitem__
    # Numéricos	            __add__, __sub__, __mul__, __mod__

    # Há um método mágico - um dunder method - que, ao ser implementado, permite que a classe seja considerada 
    # um objeto iterável: o __getitem__(). Este método define algo que é iterável e, no caso, 
    # precisaremos receber um item para que este seja repassado à lista interna que estamos utilizando, isto é, programas
    def __getitem__(self, item):
         return self._programas[item]

    # Isto porque há um dunder method que poderá ser implementado para que a lista se comporte como um sized, 
    # uma ideia de algo que possui tamanho, e que então precisará implementar um __len__() para que o len() 
    # externo possa funcionar em nossa classe.
    def __len__(self):
        return len(self._programas)
    
    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


vingadores = Filme("vingadores - guerra Infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()

print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')
print(f'{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}')
print('\n\n')

# lista = []
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    # hasattr(programa, 'duracao') = verifica se na variavel programa existe o atributo duracao

    # if hasattr(programa, 'duracao'):
    #     detalhes = programa.duracao
    # else:
    #     detalhes = programa.temporadas

    # outra forma reduzida
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas

    # print(f'{programa.nome} - {detalhes} D - {programa.likes}')

    # polimorfismo, chama o método imprime de acordo com o tipo do objeto (Filme ou Serie)
    # programa.imprime()

    # utilizando __str__ do objeto
    # representation
    print(programa)