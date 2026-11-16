class Porta:
    def abrir(self):
        print(f'Girar a maçaneta e empurrar/puxar a porta')


class Empresa:
    def abrir(self):
        print(f'Va ao portal do empreendedor com toda a documentação para abrir um CNPJ')


class Ovo:
    def abrir(self):
        print(f'Quebre a casca com um garfo e separe as partes sobre uma frigideira')


class Pedra:
    pass


# Metodo pythonico polimorfico duck typing
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f'encontrei problemas ao tentar abrir o objeto: {objeto.__class__.__name__}')


def main():
    a = Porta()
    b = Empresa()
    c = Ovo()
    d = Pedra()

    tentar_abrir(a)
    tentar_abrir(b)
    tentar_abrir(c)
    tentar_abrir(d)


if __name__ == '__main__':
    main()
