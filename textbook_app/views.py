from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
data = [{
    "title": "LOgica",
    "context": ""}]

def index(request):
    return render(request, 'textbook_app/index.html')

def textbook(request, textbook_p):
    return render(request, f'textbook_app/textbook{textbook_p}.html')