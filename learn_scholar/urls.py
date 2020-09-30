"""learn_scholar URL Configuration."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journal.urls')),
    path('', include('community.urls')),
    path('account/', include('users.urls')),
    path('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
    path('social-auth/', include('social_django.urls', namespace="social")),
]


urlpatterns += static(settings.MEDIA_URL, document.settings.MEDIA_ROOT)