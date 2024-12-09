import requests
from django.shortcuts import render

def index(request):
    endpoint = "https://brasilparticipativo.presidencia.gov.br/api"
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
    try:
        response = requests.post(endpoint, json={"query": query})
        if response.status_code == 200:
            data = response.json()
            participatory_processes = data.get("data", {}).get("participatoryProcesses", [])
            decidim_version = data.get("data", {}).get("decidim", {}).get("version", "N/A")
        else:
            participatory_processes = []
            decidim_version = "Erro ao obter a versão"
    except Exception as e:
        participatory_processes = []
        decidim_version = f"Erro: {str(e)}"

    # Renderizar os dados no template index.html
    return render(request, "index.html", {
        "participatory_processes": participatory_processes,
        "decidim_version": decidim_version,
    })
