from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Document

# Create your views here.
def index(request):
    documents = Document.objects.all()
    context = {'documents': documents}
    return render(request, 'documentation/resources.html', context)

class SearchResultsListView(ListView):
    model = Document
    context_object_name = 'documents_list'
    template_name = 'documentation/results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Document.objects.filter(
            Q(title__icontains =query) | Q(content__icontains = query) | Q(cover_image__icontains=query)
        )