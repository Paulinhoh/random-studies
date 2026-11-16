from hashlib import sha256


class ContaBancaria:
    """
    ContaBancaria:
        Cria uma conta bancaria e permite fazer saques e depositos..
    """

    def __init__(self, id: int, nome: str, saldo: float = 0, chave: str = None) -> None:
        self._id = id
        self._titular = nome
        self.__saldo = saldo

        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()

        print(f'Conta {id} criado com sucesso. Saldo: R${self.__saldo:,.2f}')

    def pede_senha(self) -> str:
        from pwinput import pwinput

        while True:
            senha = str(pwinput('Digite sua senha: ')).strip()
            if len(senha) >= 6:
                break
        return senha

    def validar_senha(self, chave: str) -> bool:
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario != self.__hash:
            return False
        return True

    def __str__(self) -> str:
        return f'Estado atual da conta {self.__dict__}'

    def deposito(self, valor) -> None:
        valor = abs(valor)
        self.__saldo += valor
        print(f'Desposito de R${valor:,.2f} autorizado na conta {self._id}.')

    def saque(self, valor: float, chave: str = None) -> None:
        valor = abs(valor)

        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'Saldo NEGADO de R${valor:.2f} na conta {self._id}: SALDO INSUFICIENTE')
                return

            self.__saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self._id}.')
        else:
            print('Senha não confere. Saque não autorizado.')

    @property
    def titular(self) -> str | None:
        return self._titular

    @titular.setter
    def titular(self, titular: str = '') -> None:
        chave = self.pede_senha()
        if self.validar_senha(chave):
            if len(titular) >= 5:
                self._titular = titular
            else:
                print('O nome deve ter no minimo 5 caracteres')


def main():
    cc = ContaBancaria(id=111, nome='Gabriel', saldo=1_200)

    print('Vou tentar sacar...')
    cc.saque(530)


if __name__ == '__main__':
    main()
