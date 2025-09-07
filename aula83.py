#class Pessoa:
#    pass

#p1 = Pessoa()

class Pessoa:
    def _init_(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def mFunc(self):
        print("Ola meu nome é " + self.nome)

p1 = Pessoa("Gabriel", 36)
p1.myFunc()            

p1.nome = "Arthur"
p1.myFunc()