from abc import ABC
from datetime import date


class Pessoa(ABC):
    def __init__(self, nome: str, nasc: int) -> None:
        self._nome = nome
        self._nascimento = None
        self._idade = None

        self.nascimento = nasc

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        raise PermissionError('Nome não pode ser alterado depois de cadastrado.')

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano: int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f'Ano {ano} é invalido.')

    @property
    def idade(self):
        return date.today().year - self.nascimento

    @idade.setter
    def idade(self, idade):
        raise PermissionError('Voce não pode alterar a idade, mude o ano de nascimento')


class Aluno(Pessoa):
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']

    def __init__(self, nome, nasc, curso: str) -> None:
        super().__init__(nome, nasc)
        self._curso = None

        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in self.__class__.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f'O curso {curso} não esta na lista de cursos oficiais.')

    def add_curso(self, curso):
        curso = curso.strip().upper()
        if curso not in self.__class__.cursos_oficiais:
            if 2 <= len(curso) <= 5:
                self.__class__.cursos_oficiais.append(curso)
            else:
                raise ValueError(f'Nome {curso}, esta fora do padrão para cursos oficiais.')
        else:
            raise ValueError(f'O curso informado ({curso}) já existe na lista de cursos oficiais.')


def main():
    try:
        aluno = Aluno('Paulo', 2012, 'ADS')
        aluno.add_curso('SI')
        aluno.curso = 'SI'

        print(f'Cursos oficiais: {aluno.cursos_oficiais}\n')
        print(f'Nome do aluno: {aluno.nome}')
        print(f'Idade do aluno: {aluno.idade}')
        print(f'Curso do aluno: {aluno.curso}')
    except Exception as erro:
        print(erro)


if __name__ == '__main__':
    main()
