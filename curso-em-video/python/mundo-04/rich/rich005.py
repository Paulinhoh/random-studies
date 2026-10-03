from rich import print
from rich.traceback import install

install()


def dividir(a, b):
    return a / b


print(dividir(50, 0))
