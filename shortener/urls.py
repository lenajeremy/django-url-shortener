from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name = 'dashboard'),
  path('register/', views.register, name = 'register'),
  path('login/', views.login_user, name = 'login'),
  path('urls/new/', views.new_url, name = 'new_url'),
  path('urls/<str:urlWhatever>', views.get_url, name = 'get_url')
]