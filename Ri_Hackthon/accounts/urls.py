from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('', LoginView.as_view(), name="login"),
    path('logout/', userLogout, name="logout"),


    path('validate-username', csrf_exempt(UsernameValidation.as_view()),
         name="validate-username"),

    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate_email'),


    path('activate/<uidb64>/<token>',
         VerificationView.as_view(), name='activate'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'
    ), name='reset_password'),
    # template_name='accounts/password_reset.html'
    path('reset_email_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    # template_name='accounts/password_reset_done.html'
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    # template_name='accounts/password_reset_confirm.html'
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
    # template_name='accounts/password_reset_complete.html'





]
