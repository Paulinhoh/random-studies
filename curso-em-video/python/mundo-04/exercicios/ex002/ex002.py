# Declaração de classes
class Gafanhoto:
    """
    Classe de Gafanhoto:
        Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
        Para criar uma nova pessoa use:
        - variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, nome='', idade=0) -> None:
        # Atributos de instancia
        self.nome = nome
        self.idade = idade

    # Métodos de instancias
    def aniversario(self) -> None:
        self.idade += 1

    def __str__(self) -> str:
        return f'{self.nome} é um Gafanhoto(a) e tem {self.idade} anos'

    def __getstate__(self) -> str:
        return f'Estado: {self.__dict__}'


# Declaração de objetos
g1 = Gafanhoto('Maria', 20)
g1.aniversario()
print(g1)

g2 = Gafanhoto('Mauro', 53)
print(g2)

print(g1.__doc__)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)
