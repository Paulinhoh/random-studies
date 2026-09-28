# =--=-=--=-=-=-=-=-=-=-=-= Exceções =--=-=--=-=-=-=-=-=-=-=-=
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Não é possível dividir por zero!'
    except TypeError:
        return 'Os valores devem ser numéricos!'
    except Exception as e:
        return f'Ocorreu um erro: {e}'
    finally:
        pass  # O bloco finally é executado independentemente de ocorrer ou não uma exceção


print(dividir(10, 0))  # Não é possível dividir por zero!
print(dividir(10, 2))  # 5.0
