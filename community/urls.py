from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap

sitemaps = {
 'posts': PostSitemap,
}

app_name = 'community'

urlpatterns = [
    # Questions page(page that shows all questions)
    path('Questa/', views.index, name = 'index'),  
    # Display Detail page for question where you can answer a question
    path('question/<int:question_id>/',views.question, name='question'),
    # Page for asking questions
    path('Questa/ask_question/',views.ask_question, name='ask_question'),
    # Page for answering a question
    path('new_answer/<int:question_id>/',views.new_answer, name='new_answer'),
    # Page for Search Results
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
    # URL for sitemap !!! Very Important
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
               name='django.contrib.sitemaps.views.sitemap')
]