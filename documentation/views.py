from django.shortcuts import render
from .models import Document

# Create your views here.
def index(request):
    documents = Document.objects.all()
    context = {'documents': documents}
    return render(request, 'documentation/resources.html', context)