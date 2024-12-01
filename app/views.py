import requests
from django.shortcuts import render

# URL da API GraphQL
GRAPHQL_URL = "https://brasilparticipativo.presidencia.gov.br/api"

# Consulta GraphQL
query = """
{
  participatoryProcesses {
    id
    title {
      translations {
        locale
        text
      }
    }
  }
  decidim {
    version
  }
}

"""

def fetch_participatory_processes():
    # Cabeçalhos da requisição
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",  
    }

    # Corpo da requisição
    json_data = {
        "query": query
    }

    # Realizando a requisição POST
    response = requests.post(GRAPHQL_URL, json=json_data, headers=headers)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        return response.json()  # Retorna os dados da resposta em formato JSON
    else:
        # Caso ocorra algum erro
        raise Exception(f"Erro na requisição: {response.status_code} - {response.text}")

def index(request):
    try:
        # Buscando os dados da API GraphQL
        data = fetch_participatory_processes()
    except Exception as e:
        data = {"error": str(e)}

    # Retorna os dados para renderizar no template
    return render(request, 'index.html', {'data': data})