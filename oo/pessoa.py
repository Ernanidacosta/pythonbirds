class Pessoa:
    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome    
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    rose = Pessoa(nome='Rose')
    ernani = Pessoa(rose, nome='Ernani')
    print(Pessoa.cumprimentar(ernani))
    print(id(rose))
    print(ernani.cumprimentar())
    print(ernani.nome)
    print(ernani.idade)
    for filho in ernani.filhos:
        print(filho.nome)
    print(ernani.__dict__)
    print(rose.__dict__)