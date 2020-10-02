from django.urls import path
from . import views

app_name = 'documantion'
urlpatterns = [
    path('resources/', views.index, name='index')
]