# =-=-=-=-=--=-=-=-= Condicionais =-=-=-=-=--=-=-=-=

# ex.: 01
tempo = str(input('quantos anos tem o seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velhor')


# ex.: 02
age = int(input('digite sua idade: '))
if age < 16:
    print('não votante')
elif (age >= 16 and age <18) or (age > 65):
    print('voto não obrigatorio')
else:
    print('voto obrigatorio!')


# ex.: 03
tempo = str(input('quantos anos tem o seu carro? '))
print('carro novo' if tempo <= 3 else 'carro veho')
