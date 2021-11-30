from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo),
    path('todos/<int:todo_id>', views.todo_detail),
    path('todos/mark_complete/<int:todo_id>', views.mark_complete),
    path('todos/today/', views.today_list),
    path('todos/anydate/', views.future_list),
]