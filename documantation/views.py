from django.shortcuts import render
from .models import Document

# Create your views here.
def index(request):
    return render(request, 'documantation/index.html')
