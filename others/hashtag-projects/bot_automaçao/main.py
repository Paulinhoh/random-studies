import pyautogui
from time import sleep
import pandas as pd

"""
pyautogui.click -> clica
pyautogui.write -> escreve
pyautogui.press -> aperta uma tecla
pyautogui.hotkey -> aperta um atalho (hotkey)

-> aprender um pouco sobre selenium
-> aprender mais sobre pyautogui
"""


def posicao_tela():
    """
    Função auxiliar somente para poder pegar a posição onde o mause
    esta, para poder saber onde o pyautoguy tem que clicar
    """
    sleep(5)
    print(pyautogui.position())


def main():
    pyautogui.PAUSE = 0.5
    url = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
    email = 'email@example.com'  # EMAIL_HERE
    password = 'senha_secreta'  # PASSWORD_HERE

    # Passo a passo do programa
    # 1. Entrar no sistema da empresa
    # abrir o navegador
    pyautogui.press('win')
    pyautogui.write('edge')
    pyautogui.press('enter')

    # entrar no site do sistema
    pyautogui.write(url)
    pyautogui.press('enter')

    # fazer uma pausa para o site carregar
    sleep(2)

    # 2. Fazer login
    pyautogui.click(x=867, y=404)
    pyautogui.write(email)

    # pyautogui.click(x=942, y=504)
    pyautogui.press('tab')
    pyautogui.write(password)

    pyautogui.press('tab')
    pyautogui.press('enter')

    sleep(2)

    # 3. Abrir a base de dados (importar o arquivo)
    tabela = pd.read_csv('produtos.csv')

    # 4. Cadastrar produtos
    for line in tabela.index:
        pyautogui.click(x=825, y=283)

        # codigo
        pyautogui.write(str(tabela.loc[line]['codigo']))
        pyautogui.press('tab')

        # marca
        pyautogui.write(str(tabela.loc[line]['marca']))
        pyautogui.press('tab')

        # tipo
        pyautogui.write(str(tabela.loc[line]['tipo']))
        pyautogui.press('tab')

        # categoria
        pyautogui.write(str(tabela.loc[line]['categoria']))
        pyautogui.press('tab')

        # preco
        pyautogui.write(str(tabela.loc[line]['preco_unitario']))
        pyautogui.press('tab')

        # custo
        pyautogui.write(str(tabela.loc[line]['custo']))
        pyautogui.press('tab')

        # obs
        if str(tabela.loc[line]['obs']) != 'nan':
            pyautogui.write(str(tabela.loc[line]['obs']))
        pyautogui.press('tab')

        # enviar
        pyautogui.press('enter')

        # voltar para o inicio da tela
        pyautogui.scroll(5000)


if __name__ == '__main__':
    auxiliar = False

    if not auxiliar:
        main()
    else:
        posicao_tela()
