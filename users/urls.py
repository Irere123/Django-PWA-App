from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    # Login page
    path('login/', views.loginPage, name= 'login'),
    # Logout page
    path('logout/', views.logoutUser, name= 'logout'),
    # Registration page
    path('register/', views.registerPage, name= 'register'),
    # Reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(), name= 'reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name= 'password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
]