from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Login page
    path('login/', views.loginPage, name= 'login'),
    # User's Questions Page
    path('myquestions/', views.myquestions, name='myquestions'),
    # Profile Page
    path('profile/', views.profile, name='profile'),
    # Logout page
    path('logout/', views.logoutUser, name= 'logout'),
    # Registration page
    path('register/', views.registerPage, name= 'register'),
    # Reset Password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='reset_password'),
    # Password Reset Done
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name='password_reset_done'),
     # Password Reset Confirmation
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
    # Password Reset Complete
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'), name='password_reset_complete'),
]