class Carteira:
    def __init__(self, valor: int | float = 0):
        self.__saldo = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("voce não tem altorização para alterar o saldo desse jeito")

    def __str__(self) -> str:
        return f'Saldo: {self.saldo}'

    def __eq__(self, outro) -> bool:
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

    def __iadd__(self, valor: int | float):
        self.__saldo += valor
        return self

    def __isub__(self, valor: int | float):
        self.__saldo -= valor
        return self

    def __le__(self, other):
        if self.__saldo <= other.__saldo:
            return True
        else:
            return False


def main():
    c1 = Carteira(100)
    c2 = Carteira(100)

    print(c1 == c2)
    c1 += c2.saldo
    print(c1)
    print(c1 == c2)


if __name__ == '__main__':
    main()
