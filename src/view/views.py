from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def analysis(request):
    return render(request, "analysis.html")
    
def selection(request):
    return render(request, "selection_page_feelings.html")
    
def about(request):
    return render(request, 'aboutus.html')

def topics(request):
    return render(request, 'selection_topics.html')
