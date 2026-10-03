class Avaliacao:

    def __init__(self, nome, diciplina, nota: float = 0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota  # Atributo protected (#)

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print('Nota invalido')


def main():
    av1 = Avaliacao('Pedro', 'Matematica', 9.5)
    av1.nota = 7.4
    print(f'{av1.nome} tirou {av1.nota} em {av1.diciplina}')


if __name__ == '__main__':
    main()
