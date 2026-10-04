"""
1. Titulo: sistema de vendas
2. Seção cadastrar vendas
    - campo data
    - campo vendedor
    - campo produto
    - campo qualidade
    - campo valor
    - botão cadastrar venda
3. Seção vendas cadastradas
    - tabela com as vendas
4. Seção dashboard
    - card/metrica -> fatturamento total
    - grafica de barra/coluna -> venda por vendedor
    - grafico de pizza -> venda por produto
"""
import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    # carregar base de vendas
    tabela_vendas = pd.read_csv('src/vendas.csv')
    valores = {'Notebook': 3500.0, 'Celular': 2000.0, 'Fone': 150.0}

    st.write("# Sistema de vendas")

    # seção de cadastro de vendas
    st.sidebar.write("## Cadastrar vendas")
    data = st.sidebar.date_input("Data")
    vendedor = st.sidebar.selectbox('Vendedor', ['Ana', 'Bruno', 'Carla'])
    produto = st.sidebar.selectbox('Produtos', ['Notebook', 'Celular', 'Fone'])
    quantidade = st.sidebar.number_input('Quantidade', value=1, step=1, min_value=1)
    valor = st.sidebar.number_input('Valor', value=quantidade * valores[produto],
                                    min_value=quantidade * valores[produto], max_value=quantidade * valores[produto])

    botao_cadastrar = st.sidebar.button('Cadastrar Venda')

    # logica de cadastro
    if botao_cadastrar:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultimo_linha = len(tabela_vendas)
        tabela_vendas.loc[ultimo_linha] = nova_venda
        tabela_vendas.to_csv('src/vendas.csv', index=False)
        st.success('Venda cadastrada!')

    # seção de visualizar vendas
    st.write("## Vendas cadastradas")
    st.dataframe(tabela_vendas)

    # seção de dashboard
    st.write("## Dashboard")

    # card / metrica -> fatturamento total
    faturamento = tabela_vendas['valor'].sum()
    st.metric('Faturamento Total', f'R$ {faturamento:.2f}')

    # grafica de barra / coluna -> venda por vendedor
    grafico_barra = px.bar(tabela_vendas, x='vendedor', y='valor', color='produto', )
    st.plotly_chart(grafico_barra)

    # grafico de pizza -> venda por produto
    grafico_pizza = px.pie(tabela_vendas, names='produto', values='valor', hole=0.5)
    st.plotly_chart(grafico_pizza)


if __name__ == '__main__':
    main()
