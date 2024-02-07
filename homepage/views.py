from django.shortcuts import render
from .models import HomePage

def index(request):
    home = HomePage.objects.first()
    return render(request, "index.html", {"home":home})