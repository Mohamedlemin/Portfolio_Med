from django.shortcuts import render
from .models import experience
# Create your views here.

# First comment
def index(request):
    experiences = experience.objects
    return render(request, 'experience/index.html', {'experiences': experiences})