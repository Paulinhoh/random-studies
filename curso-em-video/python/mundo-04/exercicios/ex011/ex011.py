class Mae:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz o PUDIM com leite condensado e caldo')

    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA no óleo de soja')


class Filha(Mae):
    def fazer_pudim(self):
        print(f'{self.nome} faz o PUDIM com leite ninho e nutela')


class Filho(Mae):
    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA na Air Fryer')


def main():
    p1 = Mae('Jaciara')
    p2 = Filho('Matheus')
    p3 = Filha('Mônica')

    p1.fazer_pudim()
    p1.fritar_coxinha()
    print()

    p2.fazer_pudim()
    p2.fritar_coxinha()
    print()

    p3.fazer_pudim()
    p3.fritar_coxinha()


if __name__ == '__main__':
    main()
