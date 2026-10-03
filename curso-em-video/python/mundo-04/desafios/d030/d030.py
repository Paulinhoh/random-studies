import hashlib


class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave: str):
        if len(chave) > 0:
            self.__hash = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Senha invalida')

    def validar_senha(self, chave: str) -> bool:
        usuario = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print('Senha confere!')
            return True
        else:
            print('Senha invalida!')
            return False


def main():
    c = Credencial()
    c.senha = 'CeV!@'
    print(c.senha)

    c.validar_senha('CeV!@')


if __name__ == '__main__':
    main()
