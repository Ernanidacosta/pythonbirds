class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def static_method():
        return 'Eu sou um staticmethod'

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de Mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    rose = Homem(nome='Rose')
    ernani = Mutante(nome='Ernani')
    print(Pessoa.cumprimentar(ernani))
    print(id(rose))
    print(ernani.cumprimentar())
    print(ernani.nome)
    print(ernani.idade)
    for filho in ernani.filhos:
        print(filho.nome)
    ernani.sobrenome = 'Costa'
    del ernani.filhos
    ernani.olhos = 2
    print(ernani.__dict__)
    print(rose.__dict__)
    Pessoa.olhos = 2
    print(Pessoa.olhos)
    print(ernani.olhos)
    print(rose.olhos)
    print(id(Pessoa.olhos), id(ernani.olhos), id(rose.olhos))
    print(Pessoa.static_method(), ernani.static_method())
    print(Pessoa.nome_e_atributos_de_classe(), ernani.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(ernani, Pessoa))
    print(isinstance(ernani, Homem))
    print(ernani.olhos)
    print(ernani.cumprimentar())
    print(rose.cumprimentar())
