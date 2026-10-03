class Termostato:
    def __init__(self) -> None:
        self.__temperatura = 24

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temp: float):
        if not temp % 0.5 == 0:
            raise ValueError('Temperatura invalida')
        elif temp < 16:
            self.__temperatura = 16
        elif temp > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = temp

    @property
    def ftemperatura(self) -> str:
        return f'{self.__temperatura}°C'


def main():
    t = Termostato()
    try:
        t.temperatura = 25.5
        print(f'A temperatura atual é {t.ftemperatura}.')
    except ValueError as erro:
        print(erro)


if __name__ == '__main__':
    main()
