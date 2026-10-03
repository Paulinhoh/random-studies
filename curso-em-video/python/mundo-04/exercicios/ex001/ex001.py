# Declaração de classes
class Gafanhoto:

    def __init__(self) -> None:
        # Atributos de instancia
        self.nome = ''
        self.idade = 0

    # Métodos de instancias
    def aniversario(self) -> None:
        self.idade += 1

    def mensagem(self) -> str:
        return f'{self.nome} é um Gafanhoto(a) e tem {self.idade} anos'



# Declaração de objetos
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 20
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
print(g2.mensagem())