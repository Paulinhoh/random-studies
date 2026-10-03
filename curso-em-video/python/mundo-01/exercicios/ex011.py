"""
    Faça um programa qe leia a largura e a altura de uma parede em metros, calcule
    a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro
    de tinta, pinta uma area de 2m².
"""

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura

litros_tinta = area / 2
print(f'Sua parede tem a dimensão de {largura}x{altura} e para pintar precisara de {litros_tinta:.2f}L')
