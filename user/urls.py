from django.urls import path
from . import views

# urls for user

urlpatterns = [

    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
]
