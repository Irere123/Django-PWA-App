"""learn_scholar URL Configuration."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Url that takes you to The Admin Page(Admin DashBoard)
    path('admin/', admin.site.urls),
    # URLS for Journal App
    path('', include('journal.urls')),
    # URLS for Community App
    path('', include('community.urls')),
    path('', include('documentation.urls')),
    # URLS for Users App
    path('account/', include('users.urls')),
    # URLS for Users App
    path('analytics/', include('analytics.urls')),
    # URLS for PWA App
    path('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
    # URLS for Social-Auth-Django
    path('social-auth/', include('social_django.urls', namespace="social")),
]


urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)