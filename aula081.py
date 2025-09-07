class Pessoa:
    def __init__(self, nome , idade) -> None:
        self.nome = nome
        self.idade = idade
    def myFunc(self):
        print("Ola meu nome é " + self.nome)
        

p1 = Pessoa("Gabriel ", 36)
p1.myFunc()        

p2 = Pessoa("Artur", 10)
p2.myFunc()