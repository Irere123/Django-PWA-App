from django.urls import path
from . import views

app_name = 'documantation'
urlpatterns = [
    path('resources/', views.index, name = 'index')
]