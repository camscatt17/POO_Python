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

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada



vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao}'
      f' - Likes: {vingadores.likes}')


atlanta = Serie('Atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporada}'
      f' - Likes: {vingadores.likes}')
