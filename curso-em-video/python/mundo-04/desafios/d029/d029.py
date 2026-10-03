class Diario:
    def __init__(self, senha='CeV!@'):
        self.__segredos = list()
        self.__senha = senha.strip()

    def escrever(self, msg: str):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha=''):
        print('Diario Liberado:')
        if senha == self.__senha:
            for cont, item in enumerate(self.__segredos):
                print(f'{cont + 1}. {item}')
        else:
            raise PermissionError('Senha incorreta! Você não pode ler o diario.')

    @property
    def senha(self):
        raise PermissionError('Acesso negado!')


def main():
    diario = Diario('Gafanhoto')

    diario.escrever('Primeira mensagem')
    diario.escrever('Segunda mensagem')
    diario.escrever('Terceira mensagem')

    try:
        diario.ler('Gafanhoto')
    except PermissionError as erro:
        print(erro)


if __name__ == '__main__':
    main()
