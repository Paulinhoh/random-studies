"""
    Operações Aritmeticas:
    +   -> soma
    -   -> subtração
    *   -> multiplicação
    /   -> divisão
    **  -> exponencial
    //  -> divisão inteira
    %   -> resto da divisão

    Ordem de precedencia:
    ()
    **
    *, /, //, %
    +, -
"""

print('=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)

print('=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(2**3)
print(3**2)
print(18%2)
print(pow(3,2))
print(81**(1/2))
print(127**(1/3))

print('=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Oi'*4, end=' >>> ')
print('=-'*3)

print('=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
name = 'paulinho'
print(f'Prazer em te conhecer {name}!')
print(f'Prazer em te conhecer {name:20}!')
print(f'Prazer em te conhecer {name:>20}!')
print(f'Prazer em te conhecer {name:<20}!')
print(f'Prazer em te conhecer {name:^20}!')
print(f'Prazer em te conhecer {name:=^20}!')

