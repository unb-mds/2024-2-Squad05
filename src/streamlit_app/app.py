import django
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'lumina.settings' 

django.setup()

import streamlit as st
import pandas as pd
import plotly.express as px
from comentario.models import Comentario
from proposta.models import Proposta

# Função para buscar dados do banco de dados
def fetch_data():
    propostas = Proposta.objects.all().values()
    comentarios = Comentario.objects.all().values()
    return pd.DataFrame(propostas), pd.DataFrame(comentarios)

st.title("Análise de Sentimentos das Propostas")

# Buscar dados
propostas_df, comentarios_df = fetch_data()

# Exibir dados brutos
st.write("### Dados das Propostas")
st.write(propostas_df)

st.write("### Dados dos Comentários")
st.write(comentarios_df)

# Análise de Sentimentos
st.write("### Análise de Sentimentos dos Comentários")

# Agrupar sentimentos por proposta
sentimentos_df = comentarios_df.groupby('proposta')['sentiment'].mean().reset_index()
sentimentos_df = sentimentos_df.merge(propostas_df, left_on='proposta', right_on='id')  # ou outro campo correto

# Gráfico de barras para média de sentimentos por proposta
fig = px.bar(sentimentos_df, x='title', y='sentiment', title="Média de Sentimentos por Proposta", labels={'sentiment': 'Média de Sentimento', 'title': 'Proposta'})
st.plotly_chart(fig)

# Gráfico de pizza para distribuição de sentimentos
sentiment_distribution = comentarios_df['sentiment'].value_counts().reset_index()
sentiment_distribution.columns = ['sentiment', 'count']
fig2 = px.pie(sentiment_distribution, values='count', names='sentiment', title="Distribuição de Sentimentos")
st.plotly_chart(fig2)

# Filtros interativos
st.write("### Filtros Interativos")
selected_proposal_id = propostas_df[propostas_df['title'] == selected_proposal]['id'].values[0]
filtered_comments = comentarios_df[comentarios_df['proposta'] == selected_proposal_id]
st.write(f"Comentários para a Proposta: {selected_proposal}")
st.write(filtered_comments)

fig3 = px.histogram(filtered_comments, x='sentiment', title=f"Distribuição de Sentimentos para {selected_proposal}")