import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# Gerando dados fictícios
data = {
    'Mês': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Vendas': [200, 220, 250, 230, 270, 300, 280, 320, 310, 350, 370, 400]
}

df = pd.DataFrame(data)

# Título da aplicação Streamlit
st.title("Exemplo de Gráficos com Matplotlib e Plotly")

# Gráfico usando Matplotlib
st.subheader("Gráfico de Linhas com Matplotlib")
fig, ax = plt.subplots()
ax.plot(df['Mês'], df['Vendas'], marker='o', color='b', linestyle='-', label='Vendas')
ax.set_xlabel('Mês')
ax.set_ylabel('Vendas')
ax.set_title('Vendas por Mês')
ax.legend()
st.pyplot(fig)

# Gráfico usando Plotly
st.subheader("Gráfico Interativo de Barras com Plotly")
fig = px.bar(df, x='Mês', y='Vendas', title="Vendas por Mês", labels={'Mês': 'Mês', 'Vendas': 'Vendas'})
st.plotly_chart(fig)

# Gráfico de linha interativo com Plotly
st.subheader("Gráfico de Linhas Interativo com Plotly")
fig = px.line(df, x='Mês', y='Vendas', title="Vendas por Mês (Interativo)", markers=True)
st.plotly_chart(fig)