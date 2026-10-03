"""
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os 'M' ou 'F'. Caso
    esteja errado peça a digitação novamente até ter um valor correto.
"""

resp = ''
while resp != 'M' and resp != 'F':
    resp = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()

    if resp != 'M' and resp != 'F':
        print('Valor invalido! Somente é aceito `M` para masculino e `F` para feminino. Tente novamente.')


print('Resposta salva com sucesso.')
