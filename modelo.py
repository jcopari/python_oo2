class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__like = 0

    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def like(self):
        return self.__like

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    
    def dar_like(self):
        self.__like += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__like = 0

    @property
    def nome(self):
        return self.__nome

    @property 
    def like(self):
       return self.__like
       
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    
    def dar_like(self):
        self.__like += 1



vingadores = Filme('vingadores', 2018, 160)
vingadores.dar_like()
print('Nome: {}, Ano: {}, Duração: {}, minutos Likes: {}'.format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.like))


atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.nome = 'Capeta'

print(f'Nome: {atlanta.nome}, Ano: {atlanta.ano}, Temporada: {atlanta.temporadas}, Likes: {atlanta.like}')