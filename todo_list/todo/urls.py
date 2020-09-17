from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list, name='todo_list'),
    path('update_todo/<int:id>/', views.update_todo, name='update_todo'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),
]
