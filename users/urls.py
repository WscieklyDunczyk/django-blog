from django.urls import path
from .views import Register, profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('rejestracja/', Register.as_view(), name='users-rejestracja'),
    path('profil/', profile, name='users-profil'),
]
