class ContaBancaria:
    """
    ContaBancaria:
        Cria uma conta bancaria e permite fazer saques e depositos..
    """

    def __init__(self, id, nome, saldo=0) -> None:
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f'Conta {id} criado com sucesso. Saldo: R${self.__saldo:,.2f}')

    def __str__(self) -> str:
        return f'Estado atual da conta {self.__dict__}'

    def deposito(self, valor) -> None:
        valor = abs(valor)
        self.__saldo += valor
        print(f'Desposito de R${valor:,.2f} autorizado na conta {self.id}.')

    def saque(self, valor: float) -> None:
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'Saldo NEGADO de R${valor:.2f} na conta {self.id}: SALDO INSUFICIENTE')
            return

        self.__saldo -= valor
        print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}.')


def main():
    c1 = ContaBancaria(111, 'Maria', 5_000)
    c1.deposito(500)
    c1.saque(100)
    c1.__saldo = 0
    print(c1)


if __name__ == '__main__':
    main()
