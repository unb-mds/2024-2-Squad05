from django.shortcuts import render
from scripts.sentiment_analysys import analyze_sentiment, str_response
from django.utils import timezone
from proposta.models import Proposta

def index(request):
    
    # Create a dummy instance of Proposta
    dummy_proposta = Proposta(
        component_id=1,
        created_at=timezone.now(),
        updated_at=timezone.now(),
        votes_count=0,
        title={"pt-BR": "Título de Exemplo"},
        body={"pt-BR": "Corpo de Exemplo"},
        comments_count=0
    )

    # Save the dummy instance to the database
    dummy_proposta.save()
    
    return render(request, 'home.html')

def analysis(request):
    if request.method == "POST":
        # Get the form data
        form_data = request.POST.get("comment")

        # Do something with the form data
        result = analyze_sentiment(form_data)
        if result == -1:
            result = "Invalid comment"

        # Return the response
        return render(request, "analysis.html", {"sentiment_result": str_response(result)})

    # If the request is not POST, render the index.html template
    return render(request, "analysis.html")
    
def selection(request):
    return render(request, "selection_page_feelings.html")
