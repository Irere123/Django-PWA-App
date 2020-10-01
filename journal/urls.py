from django.urls import path
from . import views

app_name = 'journal'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name ='topics'),
    # Detail Page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name ='topic'),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name ='new_topic'),
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name ='new_entry'),
    # Page for editing entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name ='edit_entry'),
    # Page for Deleting entries
    path('delete/<int:pk>/', views.delete, name='delete'),
    # About page
    path('about/', views.about, name='about'),
    # About page
    path('contact/', views.contact_us, name='contact'),
]