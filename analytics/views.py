from django.shortcuts import render
from .models import ObjectViewed

# Create your views here.
def index(request):
    objectsViewed= ObjectViewed.objects.all()
    context = {'objects': objectsViewed}
    return render(request, 'analytics/analytics.html', context)