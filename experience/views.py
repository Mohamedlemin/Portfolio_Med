from django.shortcuts import render
from .models import experience
# Create your views here.

# second comment test commit
def index(request):
    experiences = experience.objects
    return render(request, 'experience/index.html', {'experiences': experiences})