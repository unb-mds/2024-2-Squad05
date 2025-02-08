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



def health(request):
    return render(request, 'health.html')
    
def education(request):
    return render(request, 'education.html')
    
def security(request):
    return render(request, 'security.html')
    
def environment(request):
    return render(request, 'environment.html')
    
    
    
def culture(request):
    return render(request, 'culture.html')

def diversity(request):
    return render(request, 'diversity.html')

def economy(request):
    return render(request, 'economy.html')

def housing(request):
    return render(request, 'housing.html')

def others(request):
    return render(request, 'others.html')

def politics(request):
    return render(request, 'politics.html')

def technology(request):
    return render(request, 'technology.html')

def transportation(request):
    return render(request, 'transportation.html')
