class Numero:
    def __init__(self, valor: int | float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor *= 2

    def __str__(self) -> str:
        return f'Tenho o valor: {self.valor}'


class Texto:
    def __init__(self, txt: str = ""):
        self.texto = txt

    def dobrar(self):
        self.texto += " " + self.texto

    def __str__(self) -> str:
        return f'Tenho o texto: {self.texto}'


class Lista:
    def __init__(self, lst: list = []):
        self.valores = lst

    def dobrar(self):
        self.valores += self.valores

    def __str__(self) -> str:
        return f'Tenho os itens {self.valores} dentro da lista'


class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self) -> str:
        return f'O papel esta {"dobrado" if self.dobrado else "novo"}'


class Casa:
    pass

    def __str__(self) -> str:
        return f'Era uma casa muito engraçada'


# DUCK TYPING
def tentar_dobrar(obj):
    try:
        obj.dobrar()
    except:
        print(f'Tive dificuldades ao dobrar o objeto: {obj.__class__.__name__}')


def main():
    a = Numero(200)
    b = Texto("Gafanhoto")
    c = Lista([1, 2, 3])
    d = Papel()
    e = Casa()

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print()

    tentar_dobrar(a)
    tentar_dobrar(b)
    tentar_dobrar(c)
    tentar_dobrar(d)
    tentar_dobrar(e)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


if __name__ == '__main__':
    main()
