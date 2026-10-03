# =--=-=--=-=-=-=-=-=-=-=-= Pacotes =--=-=--=-=-=-=-=-=-=-=-=
import uteis  # pacote que eu criaria com funções uteis para o programa

num = int(input('Digite um número: '))
fat = uteis.fatorial(num)  # chamando a função fatorial do pacote uteis
print(f'O fatorial de {num} é {fat}.')
