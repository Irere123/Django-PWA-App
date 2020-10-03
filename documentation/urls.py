from django.urls import path
from . import views

app_name = 'documentation'
urlpatterns = [
    # Page for Search Results
    path('results/', views.SearchResultsListView.as_view(), name='results'),
    path('resources/', views.index, name='index')
]