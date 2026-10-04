"""
1. titulo
2. campo de mensagem (input)
3. quando o usuario enviar uma mensagem
    - mostrar a mensagem na conversa
    - mandar a mensagem para a IA responder
    - mostrar a resposta da IA na conversa

bibliotecas: streamlit e openai
"""

import streamlit as st
from openai import OpenAI


def main():
    modelo_ia = OpenAI(
        api_key='sua_chave_aqui',
        base_url='https://generativelanguage.googleapis.com/v1beta/openai'
    )

    # criar o historico de mensagens
    if not 'lista_mensagens' in st.session_state:
        st.session_state['lista_mensagens'] = []

    st.write('## ChatBot de IA')
    mensagem_usuario = st.chat_input('Escrevaa sua mensagem aqui')

    # mostrar todas as mensagens do chat
    for mensagem in st.session_state['lista_mensagens']:
        role = mensagem['role']
        content = mensagem['content']
        st.chat_message(role).write(content)

    if mensagem_usuario:
        # exibir a mensagem na tela
        # user -> usuario
        st.chat_message('user').write(mensagem_usuario)

        # salvar mensagem do usuario na sessão
        mensagem = {'role': 'user', 'content': mensagem_usuario}
        st.session_state['lista_mensagens'].append(mensagem)

        # pegar a resposta da IA
        resposta_modelo = modelo_ia.chat.completions.create(
            messages=st.session_state['lista_mensagens'],
            model='gemini-flah-lite-latest'
        )

        resposta_ia = resposta_modelo.choices[0].message.content

        # salva a resposta da IA na sessão
        mensagem = {'role': 'assistant', 'content': resposta_ia}
        st.session_state['lista_mensagens'].append(mensagem)

        # enviar a resposta da IA no chat
        # assistant -> chatbot
        st.chat_message('assistant').write(resposta_ia)


if __name__ == '__main__':
    main()
    # streamlit run main.py
