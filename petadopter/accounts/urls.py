from django.urls import path, include
from . import views  # '.' because in same folder

app_name = 'accounts'

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
