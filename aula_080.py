class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Gabriel", 36)
print("p1 " + p1.nome)
print("p1" , p1.idade)

p2 = Pessoa("Dani", 35)
print("p2 " + p2.nome)
print("p2" , p2.idade)