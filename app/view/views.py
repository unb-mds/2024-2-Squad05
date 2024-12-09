from django.shortcuts import render

def index(request):
    return render(request, "index.html", {"message": "Olá, bem vindo ao projeto Lumina"})
