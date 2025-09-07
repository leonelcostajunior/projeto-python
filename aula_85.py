class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def nomeCompleto(self):
        print(self.nome, self.sobrenome) 

p1 = Pessoa("Gabriel", "Artigas")
p1.nomeCompleto()   

class Estudante(Pessoa):
    pass

p2 = Estudante("Arthur", "Maciel")
p2.nomeCompleto()