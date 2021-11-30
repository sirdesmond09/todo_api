from django.urls import path
from . import views

urlpatterns = [
    path('users/signup/', views.add_user),
    path('users/', views.get_user),
    path('users/login/', views.user_login),
    path('users/change_passowrd/', views.reset_password),
    path('users/profile/', views.profile),
    path('users/<uuid:user_id>/', views.user_detail),
    
]