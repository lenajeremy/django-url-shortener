from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('urls/new/', views.new_url, name='new_url'),
    path('logout/', views.logout_user, name='logout'),
    path('<str:url_alias>', views.get_url, name='get_url'),
]
