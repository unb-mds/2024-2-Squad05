from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def analysis(request):
    return render(request, "analysis.html")
