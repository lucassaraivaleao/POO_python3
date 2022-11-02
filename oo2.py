class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.duracao}min - Likes: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} {self.temporadas} temporadas - Likes: {self._likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]
    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('Todo mundo em pânico', 1999, 100)
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()

atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie("Demolidor", 2016, 2)

atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()

print(f'Nome: {atlanta.nome} - Duração: {atlanta.temporadas} - Likes: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
fim_de_semana = Playlist('Fim de semana', filmes_e_series)


print(f'Tamanho da Playlist: {len(fim_de_semana)}')

print(fim_de_semana[0])

for programa in fim_de_semana:
    print(programa)

print(vingadores in fim_de_semana)

