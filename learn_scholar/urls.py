"""learn_scholar URL Configuration."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journal.urls')),
    path('', include('community.urls')),
    path('account/', include('users.urls')),
    path('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
    path('social-auth/', include('social_django.urls', namespace="social")),
]
