"""
    Crie um codigo python que testa se o site pudim.com.br está acessível pelo python, caso esteja acessível, exiba a mensagem "Site Pudim está acessível", caso não esteja acessível, exiba a mensagem "Site Pudim não está acessível".
"""

import requests

try:
    response = requests.get('https://pudim.com.br')
    if response.status_code == 200:
        print("Site Pudim está acessível")
    else:
        print("Site Pudim não está acessível")
except requests.exceptions.RequestException as e:
    print("Site Pudim não está acessível")
