from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):

    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'{self.nome} acabou de fazer matricula.')

    def estudar(self):
        print(f'{self.nome} esta estudando {self.curso} na turma {self.turma}.')


class Professor(Pessoa):

    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'Prof. {self.nome} começou a aula.')

    def estudar(self):
        print(f'{self.nome} é especialista e,  {self.especialidade} no {self.nivel}.')


class Funcionario(Pessoa):

    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'O funcionario {self.nome} acabou de bater ponto.')

    def estudar(self):
        print(f'{self.nome} se especializa para a area de {self.setor}.')


def main():
    a1 = Aluno('Paulo Henrique', 25, 'S0', 'T02')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()

    f1 = Funcionario('Claudia', 27, 'Secretaria', 'Secretaria')
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()


if __name__ == '__main__':
    main()
