class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def likes(self):
        return self._likes
    def dar_like(self):
        self._likes +=1
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'{self._nome} - {self.ano}: {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min: {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporada} temporadas: {self._likes} Likes'



vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)

atlanta = Serie('Atlanta', 2018, 2)

filmes_e_series =[vingadores,atlanta]
for programa in filmes_e_series:
    print(programa)