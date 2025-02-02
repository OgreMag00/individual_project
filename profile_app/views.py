from django.shortcuts import render
from tests_app.models import Tests

# Create your views here.

def index(request):
    username = request.user.username
    context = {'data': Tests.objects.filter(user=username)}
    return render(request, 'profile_app/index.html', context=context)
    