"""
    Crie a classe funcionario, onde podemos cadastrar nome, setor e cargo. Crie também
    um metodo que permita ao funcionario se apresentar.
"""

from rich import print


class Funcionario:
    """
    Funcionario:
    """

    # Atributos de Classe
    empresa = 'Curso em Video'

    def __init__(self, nome: str, setor: str, cargo: str) -> None:
        # Atributos de Instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f'Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}.'

    def get_empresa(self) -> str:
        return self.__class__.empresa

    def set_empresa(self, empresa: str) -> None:
        self.__class__.empresa = empresa


def main():
    c1 = Funcionario('Maria', 'Administação', 'Diretora')
    print(c1.apresentacao())

    c2 = Funcionario('Pedro', 'TI', 'Programador')
    c2.set_empresa('Hostnet')
    print(c2.apresentacao())


if __name__ == '__main__':
    main()
