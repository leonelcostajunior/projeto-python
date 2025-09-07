class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
    
    def nomeCompleto(self):
        print(self.nome, self.sobrenome)

class Estudante(Pessoa):
    def __init__(self, nome, sobrenome, anoGrad):
        super().__init__(nome, sobrenome)
        self.anoGrad = anoGrad
    
    def bemVindo(self):
        print("Bem vindo", self.nome, self.sobrenome, "para a turma de", self.anoGrad)

x = Estudante("Gabriel", "Artigas", 2021)
x.nomeCompleto()
x.bemVindo()
# print(x.anoGrad)