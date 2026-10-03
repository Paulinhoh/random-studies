from abc import ABC, abstractmethod


class Funcionario(ABC):
    sal_min = 1_612
    inss = 7.5

    def __init__(self, nome, sal_bruto=0, salario=0) -> None:
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario

    @abstractmethod
    def calc_sal(self) -> None:
        pass

    def analisa_sal(self) -> None:
        print(
            f'O salario de {self.nome} é de R${self.salario:,.2f} e corresponde a {self.salario / self.__class__.sal_min:.1f} salarios minimos')


class Horista(Funcionario):

    def __init__(self, nome, valor_hora=7.37, horas_trab=220) -> None:
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self) -> None:
        self.salario = self.sal_bruto - (self.sal_bruto * (self.__class__.inss / 100))


class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto, )

    def calc_sal(self) -> None:
        self.salario = self.sal_bruto - (self.sal_bruto * (self.__class__.inss / 100))


def main():
    f1 = Horista('Paulo', 12, 200)
    f1.calc_sal()
    f1.analisa_sal()

    f2 = Mensalista('Amanda', 9500)
    f2.calc_sal()
    f2.analisa_sal()


if __name__ == '__main__':
    main()
