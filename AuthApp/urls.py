"""blango URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
import AuthApp.views

# other imports
from django_registration.backends.activation.views import RegistrationView
from AuthApp.forms import MovieRegistrationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/profile/", AuthApp.views.profile, name="profile"),
    path("accounts/register/",
        RegistrationView.as_view(form_class=MovieRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/signup/",
        RegistrationView.as_view(form_class=MovieRegistrationForm),
        name="django_registration_register",
    ),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='AuthApp/password_reset_form.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='AuthApp/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='AuthApp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='AuthApp/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='AuthApp/logout.html'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("django_registration.backends.activation.urls")),
]
