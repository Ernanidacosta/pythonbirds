class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def static_method():
        return 'Eu sou um staticmethod'

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    rose = Pessoa(nome='Rose')
    ernani = Homem(rose, nome='Ernani')
    print(Pessoa.cumprimentar(ernani))
    print(id(rose))
    print(ernani.cumprimentar())
    print(ernani.nome)
    print(ernani.idade)
    for filho in ernani.filhos:
        print(filho.nome)
    ernani.sobrenome = 'Costa'
    del ernani.filhos
    ernani.olhos = 1
    del ernani.olhos
    print(ernani.__dict__)
    print(rose.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(ernani.olhos)
    print(rose.olhos)
    print(id(Pessoa.olhos), id(ernani.olhos), id(rose.olhos))
    print(Pessoa.static_method(), ernani.static_method())
    print(Pessoa.nome_e_atributos_de_classe(), ernani.nome_e_atributos_de_classe())
