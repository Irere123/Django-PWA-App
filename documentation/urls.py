from django.urls import path
from . import views

app_name = 'documentation'
urlpatterns = [
    
    path('resources/', views.index, name='index')
]