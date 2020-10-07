from django.urls import path
from . import views

app_name='analytics'

urlpatterns = [
    path('site/', views.index, name='index')
]