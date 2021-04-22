from . import views
from django.urls import path, include

app_name = 'adopter'

urlpatterns = [
    path('', views.PostList, name='list'),
    path('create/', views.PostCreate, name='create'),
    path('<slug:slug>/', views.PostDetail, name='detail'),
]
