from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'tests_app/index.html')


def test(request, test_num):
    return render(request, f'tests_app/test/{test_num}.html')
