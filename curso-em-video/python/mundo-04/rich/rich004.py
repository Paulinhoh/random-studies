from rich import print
from rich import inspect

inspect(int)
print()
print(int.__doc__)
print()
inspect(int, all=True)

print()
print('=-=' * 20)
print()


class ContaBancaria:
    """
    ContaBancaria:
        Cria uma conta bancaria e permite fazer saques e depositos..
    """

    def __init__(self, id, nome, saldo=0) -> None:
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {id} criado com sucesso. Saldo: R${self.saldo:,.2f}')

    def __str__(self) -> str:
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

    def deposito(self, valor) -> None:
        self.saldo += valor
        print(f'Desposito de R${valor:,.2f} autorizado na conta {self.id}.')

    def saque(self, valor: float) -> None:
        if valor > self.saldo:
            print(f'Saldo NEGADO de R${valor:.2f} na conta {self.id}: SALDO INSUFICIENTE')
            return

        self.saldo -= valor
        print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}.')


c1 = ContaBancaria(112, 'Gustavo', 3000)
inspect(c1)
